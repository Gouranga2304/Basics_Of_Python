print("Chatbot: Hi! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello there!")
    elif "how are you" in user_input:
        print("Chatbot: I'm just a bunch of code, but I'm doing great!")
    elif "name" in user_input:
        print("Chatbot: I'm a simple Python chatbot.")
    else:
        print("Chatbot: Sorry, I don't understand that.")