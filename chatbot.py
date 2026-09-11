"""
Task 4: Basic Chatbot
A simple rule-based chatbot.
Concepts used: if-elif, functions, loops, input/output.
"""


def get_response(user_input):
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif "name" in text:
        return "I'm a simple chatbot."
    else:
        return "Sorry, I don't understand that."


def run_chatbot():
    print("Chatbot: Hi! Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    run_chatbot()
