# Updated basic LLM code for system prompt testing
# Modified by Katherina L Jesek
# Any modifications to the original code are provided under MIT License

# Features added:
#  Updating prompt and model from within the program
#  Automated logging of conversations
#   (manual mode and automatic looping mode with fuzzy match)

import json
import os
import sys
import requests
from dotenv import load_dotenv  # needed to keep API key secret while using Git
from difflib import SequenceMatcher, get_close_matches  # for fuzzy matching

API_URL = "https://api.aimlapi.com/v1/chat/completions"
MODEL = "google/gemma-3-4b-it"

prompt_change_flag = False
message_box = []
multi_run = False
loop_msg = "Solve for y in the equation y=(x+1)/3 for x=8, \nproviding no additional information aside from the correct answer. \nGive answers in the format of 'y=i'"
success_condition = "y=3"
similarity_to_consider_success = 0.75
max_runs = 5


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
    new_entry = [system_prompt, success, message_box, MODEL]
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
            "temperature": 0.7,
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
    global prompt_change_flag, message_box, MODEL, multi_run, loop_msg, success_condition, similarity_to_consider_success, max_runs
    api_key = get_api_key()

    system_prompt = (
        "You are a helpful, friendly assistant. "
        "Answer questions clearly and concisely."
    )

    prompt_database, msg_database = prompt_database_init()

    conversation: list[dict] = []

    print("Chatbot ready! Type your message and press Enter.")
    print("Commands: 'quit' to exit, 'clear' to reset conversation,\n 'change' to update system prompt, 'success' to record a good prompt, \n'fail' to record a bad one, 'loop' or 'repeat' to enter/exit auto mode")
    ticker = 0
    user_input = ""
    while True:
        try:
            if prompt_change_flag:
                user_input = input("New system prompt: ").strip()
            elif ticker >= max_runs or not multi_run:
                user_input = input("You: ").strip()
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
                similarity_to_consider_success_n = input("Similarity threshold for success (ie. '0.5' to accept 50%+ similarity as success): ")
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

        if not conversation:
            user_content = f"[Instructions: {system_prompt}]\n\n{user_input}"


        else:
            user_content = user_input
        last_conversation = conversation.copy()
        conversation.append({"role": "user", "content": user_content})
        message_box.append({"role": "user", "content": user_content})
        reply = chat(api_key, conversation)

        if reply:
            conversation.append({"role": "assistant", "content": reply})
            message_box.append({"role": "assistant", "content": reply})
            print(f"\nAssistant: {reply}\n")
            if multi_run:
                # get a similarity profile between the reply and the success condition
                likeness_ratio = SequenceMatcher(None, reply, success_condition).ratio()
                likeness_ratio_round = round(likeness_ratio, 2)
                if likeness_ratio > similarity_to_consider_success:
                    hit_or_miss = True
                else:
                    hit_or_miss = False
                add_prompt_to_database(hit_or_miss, system_prompt, prompt_database, message_box, msg_database)
                conversation = last_conversation
                message_box = last_conversation
                ticker += 1
        else:
            conversation.pop()


if __name__ == "__main__":
    main()
