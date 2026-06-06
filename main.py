# Updated basic LLM code for system prompt testing
# Modified by Katherina L Jesek
# Any modifications to the original code are provided under MIT License

# Features added:
#  Updating prompt and model from within the program
#  Automated logging of conversations
#   (type "success" or "fail" to save a response you score manually)
#   (or type "loop" to start an automated trial, using fuzzy matching
#   to determine success. using deterministic questions with single, clear
#   answers will give you your best data)

import questionpipe as qp
import json
import os
import sys
import requests
import copy
from dotenv import load_dotenv  # needed to keep API key secret while using Git
from difflib import SequenceMatcher, get_close_matches  # for fuzzy matching
import finishedsound as fs

API_URL = "https://api.aimlapi.com/v1/chat/completions"
MODEL = "nvidia/nemotron-nano-9b-v2"
TEMPERATURE = 0.3

prompt_change_flag = False
message_box = []
multi_run = False
loop_msg = ""
success_condition = ""
similarity_to_consider_success = 0.75
max_runs = 5 
system_prompt = (
        "You are a helpful AI assistant." +
        "I'm going to ask you some test questions to determine your intelligence," +
        "I need you to answer correctly and without providing additional information, characters, or explanations. Keep answers contained to a single word wherever possible, except when specified otherwise in the question. If an answer is numerical, use numerical digits."
    )


def prompt_database_init():  # open the list from the db file
    try:
        with open('database.json', 'r') as file:
            loaded_database = json.load(file)
    except FileNotFoundError:
        loaded_database = []
    msg_database = []
    return loaded_database, msg_database


def prompt_database_save(prompt_database, msg_database):  # save the list of prompts
    with open('database.json', 'w') as file:
        json.dump(prompt_database, file, indent=2)


def add_prompt_to_database(success, system_prompt, prompt_database, message_box, msg_database):
    new_entry = [system_prompt, success, copy.deepcopy(message_box), MODEL, TEMPERATURE]
    prompt_database.append(new_entry)
    new_entry_msg = message_box
    prompt_database_save(prompt_database, msg_database)
    print("Saved to database!")


def get_api_key() -> str:
    load_dotenv()  # load environment variables
    #api_key = os.getenv("AIML_API_KEY")
    test_call = os.environ.get("TEST_CALL")
    api_key = os.environ.get("AIML_API_KEY") or os.environ.get("AIMLAPI_API_KEY")
    if test_call:
        print(test_call)  # test our load with a print
    else:
        print("Failed to load environment variables")  # return an error
    if not api_key:
        print("Missing API key. Set AIML_API_KEY or AIMLAPI_API_KEY, then run again.")
        print("Example: export AIML_API_KEY='your-key-here'")
        sys.exit(1)
    return api_key


def chat(api_key: str, messages: list[dict]) -> str:
    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": messages,
            "temperature": TEMPERATURE,
            "max_tokens": 1024,
        },
        timeout=120,
    )

    if not response.ok:
        print(f"\nAPI Error ({response.status_code}): {response.text}")
        multi_run = False
        return ""

    data = response.json()
    return data["choices"][0]["message"]["content"]


def main() -> None:
    global prompt_change_flag, message_box, MODEL, multi_run, loop_msg, success_condition, similarity_to_consider_success, max_runs, system_prompt
    api_key = get_api_key()

    prompt_database, msg_database = prompt_database_init()

    conversation: list[dict] = []

    print("Chatbot ready! Type your message and press Enter.")
    print("Commands:\n'quit' to exit, \n'clear' to reset conversation, \n'change' to update system prompt, \n'success' to record a good prompt, \n'fail' to record a bad one, \n'loop' or 'repeat' to enter/exit auto mode, \n'model' to switch the model, \n'dump' to open the question pipeline and feed it automatically\n*note: 'dump' can take a while to run, please be patient \nand do it on a stable wi-fi connection")
    ticker = 0
    user_input = ""
    while True:
        try:
            if prompt_change_flag:
                user_input = input("New system prompt: ").strip()
            elif ticker >= max_runs or not multi_run:
                if not qp.question_pipe_open:
                    multi_run = False
                    user_input = input("You: ").strip()
                else:
                    if qp.question_pipe_index < len(qp.question_pipe):
                        qp.question_pipe_index += 1
                    else:
                        multi_run = False
                        continue
                ticker = 0
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        else:
            last_user_input = user_input.lower()
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if user_input.lower() == "model":
            new_model = input("Switching out my brain, huh?\nNew model address: ")
            if new_model:
                MODEL = new_model
            user_input = ""
            continue

        if user_input.lower() == "clear":
            conversation = []
            message_box = []
            print("Conversation cleared.\n")
            continue

        if user_input.lower() == "print":
            print(conversation)
            print(message_box)
            continue

        if user_input.lower() == 'loop' or user_input.lower() == 'repeat':
            if not multi_run:
                multi_run = True
            else:
                multi_run = False
            if multi_run:
                print("Enter parameters for automatic trial")
                loop_msg_n = input("Question for the model\n(ie. 'Solve for y in the equation y=(x+1)/3 for x=8 providing no additional information\naside from the correct answer.' : ")  # what message is sent to the model repeatedly
                if loop_msg_n:
                    loop_msg = loop_msg_n
                success_condition_n = str(input("Success condition (ie. '3'): "))  # what the program should mark as "true" in the JSON file
                if success_condition_n:
                    success_condition = success_condition_n
                similarity_to_consider_success_n = float(input("Similarity threshold for success (ie. '0.5' to accept 50%+ similarity as success): "))
                if similarity_to_consider_success_n:
                    similarity_to_consider_success = similarity_to_consider_success_n
                max_runs_n = int(input("How many times should we try it?: "))
                if max_runs_n:
                    max_runs = max_runs_n
                model_to_test = input("What model should we test it on?: ")
                if model_to_test:
                    MODEL = model_to_test
                user_input = loop_msg
                continue

        if user_input.lower() == 'success':
            add_prompt_to_database(True, system_prompt, prompt_database, message_box, msg_database)
            conversation = []
            message_box = []
            continue

        if user_input.lower() == 'alarm' or user_input.lower() == 'sound':
            fs.sound_on_off()
            continue

        if user_input.lower() == 'fail':
            add_prompt_to_database(False, system_prompt, prompt_database, message_box, msg_database)
            conversation = []
            message_box = []
            continue
        if user_input.lower() == 'undo':
            if last_conversation:
                conversation = last_conversation
            else:
                conversation = []
            continue

        if user_input.lower() == "change":  # new command to change sysprompt
            prompt_change_flag = True
            continue

        if user_input.lower() == "dump":
            multi_run = True
            user_content = qp.question_pipe[1]
            success_condition = qp.qp_answer_key[1]
            similarity_to_consider_success = qp.qp_match_value[1]
            qp.question_pipe_open = True

        if qp.question_pipe_open:
            try:
                ind = qp.question_pipe_index
                user_input = qp.question_pipe[ind]
                success_condition = qp.qp_answer_key[ind]
                similarity_to_consider_success = qp.qp_match_value[ind]
            except IndexError:
                print("Automated question dump done! Check database.json for logs.")
                fs.finished_sound()
                multi_run = False
                qp.question_pipe_open = False
                qp.question_pipe_index = 1
                continue


        if not conversation:
            user_content = f"[Instructions: {system_prompt}]\n\n{user_input}"

        else:
            user_content = user_input
        last_conversation = copy.deepcopy(conversation)
        last_msg_box = copy.deepcopy(message_box)
        conversation.append({"role": "user", "content": user_content})
        message_box.append({"role": "user", "content": user_content})
        reply = chat(api_key, conversation)

        if reply:
            conversation.append({"role": "assistant", "content": reply})
            message_box.append({"role": "assistant", "content": reply})
            print(f"\nAssistant: {reply}\n")
            try:
                cleaned_reply = reply.split('</think>', 1)[1]
            except IndexError:
                try:
                    cleaned_reply = reply.split('\n')[1] # THIs IS WHERE I LEFT OFF LOL
                except IndexError:
                    cleaned_reply = reply
            cleaned_reply = cleaned_reply.replace('\n', '')
            cleaned_reply = cleaned_reply.lower()
            if multi_run:
                print("extracted answer: " + cleaned_reply)
                # get a similarity profile between the reply and the success condition
                likeness_ratio = SequenceMatcher(None, cleaned_reply, success_condition.lower()).ratio()
                likeness_ratio_round = round(likeness_ratio, 2)
                if likeness_ratio > similarity_to_consider_success:
                    hit_or_miss = True
                else:
                    hit_or_miss = False
                add_prompt_to_database(hit_or_miss, system_prompt, prompt_database, message_box, msg_database)
                if qp.question_pipe_open:
                    conversation = []
                    message_box = []
                else:
                    conversation = last_conversation
                    message_box = last_msg_box
                ticker += 1
        else:
            conversation.pop()


if __name__ == "__main__":
    main()
