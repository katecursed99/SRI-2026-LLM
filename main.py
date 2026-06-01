import os
import sys
import requests
from dotenv import load_dotenv  # needed to keep API key secret while using Git

load_dotenv()  # load environment variables
api_key = os.getenv("AIML_API_KEY")
test_call = os.getenv("TEST_CALL")

if test_call:
    print(test_call)  # test our load with a print
else:
    print("Failed to load environment variables") # default return

API_URL = "https://api.aimlapi.com/v1/chat/completions"
MODEL = "google/gemma-3-4b-it"


def get_api_key() -> str:
    api_key = os.environ.get("AIML_API_KEY") or os.environ.get("AIMLAPI_API_KEY")
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
        return ""

    data = response.json()
    return data["choices"][0]["message"]["content"]


def main() -> None:
    api_key = get_api_key()

    system_prompt = (
        "You are a helpful, friendly assistant. "
        "Answer questions clearly and concisely."
    )

    conversation: list[dict] = []

    print("Chatbot ready! Type your message and press Enter.")
    print("Commands: 'quit' to exit, 'clear' to reset conversation.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if user_input.lower() == "clear":
            conversation = []
            print("Conversation cleared.\n")
            continue

        

        if not conversation:
            user_content = f"[Instructions: {system_prompt}]\n\n{user_input}"
        else:
            user_content = user_input

        conversation.append({"role": "user", "content": user_content})

        reply = chat(api_key, conversation)

        if reply:
            conversation.append({"role": "assistant", "content": reply})
            print(f"\nAssistant: {reply}\n")
        else:
            conversation.pop()


if __name__ == "__main__":
    main()
