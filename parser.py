import json
import io
import plotter
import questionpipe as qp
import pricelist as pl
import lettergrade as lg

# Globals
#  note: it's good practice to expose these directly to functions *as little as
#  possible*, and send them as parameters instead. when calling explicit global
#  you create what's known as "spaghetti code" because it becomes "tangled"
#  and adds more work when you try to reuse the code later! - Kate
Path = 'database.json'
Data_Collector = {}


def LoadData(path):
    while True:
        try:
            with open(path, 'r') as file:  # Open the JSON file in read mode
                raw_data = json.load(file)
                new_list = raw_data.copy()  # Duplicate the list
                return new_list  # Send it back
        except FileNotFoundError:
            print("No JSON found!")
            input("What's the file's path again?:")


def ParseData(parser_data, data_collector):
    question_number = 0
    question = ""  # Initialize this so the first check can run
    for trial in parser_data:  # Run through each trial saved to the file
        success_value = trial[1]  # Check the list for model name
        model_name = trial[3]  # Check list for correctness of answer
        temperature = trial[4]  # Get the model temperature used for the trial
        whole_message = trial[2][0]["content"]  # Message we sent & sys prompt
        msg_broken = whole_message.split('\n', 1)  # Msg & prompt divorced :(
        sys_prompt = msg_broken[0]  # Now we have all the data we need
        if question != msg_broken[1].replace('\n', ""):  # Check if updating
            question = msg_broken[1].replace('\n', "")  # Strip extra newline
        data_collector = PostToCollector(model_name, question, success_value,
                                         sys_prompt, data_collector,
                                         question_number,temperature)
    data_collector = CalculateTotals(data_collector)
    return data_collector


def CalculateTotals(data_collector):
    for model_name in data_collector:  # for each model's entry
        model = data_collector[model_name]
        correct_total = 0
        total_attempts = 0
        for question in model:  # for each question the model was asked
            # total our corrects & tries
            correct_total += model[question]["Correct"]
            total_attempts += (model[question]["Correct"]
                               + model[question]["Incorrect"])
        score = correct_total / total_attempts  # calculate a correctness score
        model["TotalCorrect"] = correct_total
        model["TotalAttempts"] = total_attempts
        model["Score"] = score
    return data_collector


def PostToCollector(model_name, question, success_value, sys_prompt,
                    data_collector, question_num, temperature):
    if success_value:
        success = "Correct"  # convert number to text
    else:
        success = "Incorrect"
    if model_name not in data_collector:  # initialize step-by-step to
        data_collector[model_name] = {}   # avoid overwriting
        
    if question not in data_collector[model_name]:
        data_collector[model_name][question] = {}
        data_collector[model_name][question]["QuestionNumber"] = question_num
    if success not in data_collector[model_name][question]:
        data_collector[model_name][question]["Correct"] = 0
        data_collector[model_name][question]["Incorrect"] = 0
        data_collector[model_name][question]["Temperature"] = temperature
    data_collector[model_name][question][success] += 1
    return data_collector


Models_For_Graph = []
Models_With_Letter_Scores_For_Bar = []
Score_Datapoints_For_Graph = []
Price_List_For_Graph = []
Question_List_For_Graph = {}
Letter_Grades_For_Graph = []



def CalculateDataPoints(Models_For_Graph, Score_Datapoints_For_Graph, Question_List_For_Graph, Letter_Grades_For_Graph, Models_With_Letter_Scores_For_Bar, Price_List_For_Graph):
    parser_data = LoadData(Path)
    ParseData(parser_data, Data_Collector)

    SUMMARY_KEYS = {"TotalCorrect", "TotalAttempts", "Score", "AverageCost"}

    # First pass: just calculate AverageCost for each model
    for model in Data_Collector:
        price_info = pl.model_prices.get(model, {})
        Data_Collector[model]["AverageCost"] = price_info.get("avg", 0)

    # Sort by cost
    Data_Collector_Sorted = sorted(
        Data_Collector.items(),
        key=lambda x: x[1].get("AverageCost", 0)
    )

    # Second pass: build all graph lists in sorted order
    for model, model_data in Data_Collector_Sorted:
        Models_For_Graph.append(model)
        model_score = model_data.get("Score", 0)

        print(model_score)
        model_letter_score = lg.CalculateLetterGrade(model_score)
        Letter_Grades_For_Graph.append(model_letter_score)
        Models_With_Letter_Scores_For_Bar.append(model+" "+model_letter_score)
        Score_Datapoints_For_Graph.append(model_score)
        Price_List_For_Graph.append(model_data.get("AverageCost", 0))

        # Build question scores in this same sorted order
        for original_key, value in model_data.items():
            clean_key = original_key.rstrip()
            if clean_key in SUMMARY_KEYS:
                continue

            if isinstance(value, dict) and "Correct" in value:
                correct = value.get("Correct", 0)
                incorrect = value.get("Incorrect", 0)
                attempts = correct + incorrect
                question_score = correct / attempts if attempts > 0 else 0

                # setdefault ensures the inner dict exists
                # Since we're iterating models in sorted order, 
                # the inner dict will be populated in sorted order
                Question_List_For_Graph.setdefault(clean_key, {})[model] = question_score
    for question in Question_List_For_Graph:
        Question_List_For_Graph[question] = dict(
            reversed(Question_List_For_Graph[question].items())
        )

    return Models_For_Graph, Score_Datapoints_For_Graph, Question_List_For_Graph, Letter_Grades_For_Graph, Models_With_Letter_Scores_For_Bar, Price_List_For_Graph



Models_For_Graph, Score_Datapoints_For_Graph, Question_List_For_Graph, Letter_Grades_For_Graph, Models_With_Letter_Scores_For_Bar, Price_List_For_Graph = CalculateDataPoints(Models_For_Graph, Score_Datapoints_For_Graph, Question_List_For_Graph, Letter_Grades_For_Graph, Models_With_Letter_Scores_For_Bar, Price_List_For_Graph)
plotter.PriceAgainstIntelligence(Models_For_Graph, Score_Datapoints_For_Graph, Price_List_For_Graph)

plotter.BarGraphFromData(Models_With_Letter_Scores_For_Bar, Score_Datapoints_For_Graph)
plotter.HeatMap(Question_List_For_Graph, qp.Unique_Questions)
