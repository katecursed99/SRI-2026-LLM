import json

def LoadData(path):
    while True:
        try:
            with open(path, 'r') as file:  # Open the JSON file in read mode
                raw_data = json.load(file)
                new_list = raw_data.copy()  # Duplicate the list
                return new_list  # Send it back
        except FileNotFoundError:
            print("No JSON found!")
            path = input("What's the file's path again?:")


def NeedsReview(trial):
    if len(trial[2][1]["content"].split()) > 2 and not trial[1]:
        try:
            print(trial[4])
            return True
        except IndexError:
            return True


def ParseData(parser_data, reviewer_name):
    question_number = 0
    question = ""  # Initialize this so the first check can run
    num_of_reviews = 0
    num_of_entries = 0
    current_review = 0
    for trial in parser_data:  # run through once to count how many are needed
        num_of_entries += 1
        if NeedsReview(trial):
            num_of_reviews += 1
    for trial in parser_data:  # Run through each trial saved to the file
        if NeedsReview(trial):
            current_review += 1
            print("\n\n\n**Review #"+str(current_review)+"/"+str(num_of_reviews)+"**")
            print("Out of total entries in DB: "+str(num_of_entries))
        success_value = trial[1]  # Check the list for model name
        model_name = trial[3]  # Check list for correctness of answer
        temperature = trial[4]  # Get the model temperature used for the trial
        whole_message = trial[2][0]["content"]  # Message we sent & sys prompt
        msg_broken = whole_message.split('\n', 1)  # Msg & prompt divorced :(
        bot_message = trial[2][1]["content"]  # Message returned from bot
        sys_prompt = msg_broken[0]  # Now we have all the data we need
        if question != msg_broken[1].replace('\n', ""):  # Check if updating
            question = msg_broken[1].replace('\n', "")  # Strip extra newline
        bot_message_cleaned = ExtractAnswers(bot_message)
        SendForReview(question, bot_message_cleaned, success_value, bot_message, trial, reviewer_name)
        print(bot_message_cleaned)


def SendForReview(question, msg, success_value, bot_message, trial, reviewer_name):
    # find the high-information (aka unexpected) messages parsed
    while True:
        if NeedsReview(trial):
            print("Hello "+reviewer_name+"! Please review the following. The model name has been intentionally obscured so as to not bias your results.\n\nUse 'info' to see the rest of the bot's answer if the parser looks like it's grabbing the wrong chunks.")
            print("\nQUESTION: "+question)
            print("\nANSWER: "+msg)
            print("\nMachine grader marked: **INCORRECT**")
            change_answer_flag = input("\nDoes this need to be edited? y/n ")
            if change_answer_flag.lower() == "info":
                print("\nFull response was: "+bot_message)
                change_answer_flag = input("\nDoes this need to be edited? y/n ")
            elif change_answer_flag.lower() == "y":
                change_confirmation = input("\nAre you sure? Only hit 'y' if the bot was unfairly marked incorrect. y/n \n")
                if change_confirmation == "y":
                    trial[1] = not trial[1]
                    break
                else:
                    break
            elif change_answer_flag == "n":
                sign_flag = input("Sign off that you\na) have reviewed this question and \nb) believe the filter was accurate? y/n \n")
                if sign_flag.lower() == 'y':
                    trial.append(reviewer_name)
                break
        else:
            break


def ExtractAnswers(reply):
    try:
        cleaned_reply = reply.split('</think>', 1)[1]
    except IndexError:
        try:
            cleaned_reply = reply.split('\n')[0]
        except IndexError:
            cleaned_reply = reply
    cleaned_reply = cleaned_reply.replace('\n', '')
    if cleaned_reply == "" or cleaned_reply == " " or len(cleaned_reply.split(' ')) > 2:
        try:
            cleaned_reply = reply.split('\n')[-1]
            if len(cleaned_reply.split(' ')) > 1 or len(cleaned_reply.split(' ')) < 0:
                cleaned_reply = reply.split('\n')[1]
        except IndexError:
            try:
                cleaned_reply = reply.split(':')[-1]
            except IndexError:
                try:
                    cleaned_reply = reply.split('\n')[0]
                except IndexError:
                    cleaned_reply = reply
    if cleaned_reply == "" or len(cleaned_reply.split(' ')) > 2:
        cleaned_reply = reply
    if reply == "":
        cleaned_reply = "Failure to follow directions, mark incorrect"
    cleaned_reply = cleaned_reply.replace('\n', '')
    cleaned_reply = cleaned_reply.lower()
    return cleaned_reply


reviewer_name = input("What is your name? ")
data_file = LoadData("database.json")
ParseData(data_file, reviewer_name)
