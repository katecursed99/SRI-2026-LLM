import json
import io

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
        whole_message = trial[2][0]["content"]  # Message we sent & sys prompt
        msg_broken = whole_message.split('\n', 1)  # Msg & prompt divorced :(
        sys_prompt = msg_broken[0]  # Now we have all the data we need
        if question != msg_broken[1].replace('\n', ""):  # Check if updating
            question_number += 1  # Number the new question
            question = msg_broken[1].replace('\n', "")  # Strip extra newline
        data_collector = PostToCollector(model_name, question, success_value,
                                         sys_prompt, data_collector,
                                         question_number)
    data_collector = CalculateTotals(data_collector)
    return data_collector


def CalculateTotals(data_collector):
    for model_name in data_collector:  # for each model's entry
        model = data_collector[model_name]
        correct_total = 0
        total_attempts = 0
        total_questions = 0
        for question in model:  # for each question the model was asked
            correct_total += model[question]["Correct"]  # total our corrects & tries
            total_attempts += (model[question]["Correct"]+model[question]["Incorrect"])
            if model[question]["QuestionNumber"] > total_questions:  # use highest q-number
                total_questions = model[question]["QuestionNumber"]  # to determine total q's
        score = correct_total / total_attempts  # calculate a score
        model["TotalCorrect"] = correct_total
        model["TotalAttempts"] = total_attempts
        model["UniqueQuestionsAsked"] = total_questions
        model["Score"] = score
    return data_collector


def PostToCollector(model_name, question, success_value, sys_prompt,
                    data_collector, question_number):
    if success_value:
        success = "Correct"  # convert number to text
    else:
        success = "Incorrect"
    if model_name not in data_collector:  # initialize step-by-step to
        data_collector[model_name] = {}   # avoid overwriting
    if question not in data_collector[model_name]:
        data_collector[model_name][question] = {}
        data_collector[model_name][question]["QuestionNumber"] = question_number
    if success not in data_collector[model_name][question]:
        data_collector[model_name][question]["Correct"] = 0
        data_collector[model_name][question]["Incorrect"] = 0
    data_collector[model_name][question][success] += 1
    return data_collector


parser_data = LoadData(Path)  # Get the data from the Json file
ParseData(parser_data, Data_Collector)  # Process it to a usable dataset
print(Data_Collector)
