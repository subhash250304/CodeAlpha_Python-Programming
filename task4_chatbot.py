def chatbot():
    print("🤖 Simple Chatbot! Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi"]:
            print("Bot: Hello! How can I help you?")
        elif user in ["how are you", "how are you doing"]:
            print("Bot: I'm doing great, thanks!")
        elif user in ["bye", "exit"]:
            print("Bot: Goodbye! Have a nice day 😊")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
