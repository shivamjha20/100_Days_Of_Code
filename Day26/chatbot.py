def chatbot():
    print("Hello! I am your basic chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Bot: I'm doing great, thanks for asking!")
        elif "name" in user_input:
            print("Bot: I'm a simple chatbot written in Python.")
        elif "weather" in user_input:
            print("Bot: I can't check the weather yet, but it's always sunny in code!")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
