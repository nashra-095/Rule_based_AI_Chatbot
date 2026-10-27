
# Rule-Based AI Chatbot

# Knowledge base: predefined intents and responses
knowledge_base = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi! Nice to meet you.",
    "how are you": "I am fine. Thanks for asking!",
    "what is your name": "My name is PyBot.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "thank you": "You are welcome!",
    "help": "You can ask me about AI, Python, or greetings."
}

print("===== Welcome to PyBot =====")
print("Type 'bye' or 'exit' to end the chat.")

# Continuous input loop
while True:
    user_input = input("You: ")

    # Sanitize input: remove extra spaces and lowercase
    user_input = user_input.strip().lower()

    # Exit strategy
    if user_input == "bye" or user_input == "exit":
        print("PyBot: Goodbye! Have a nice day.")
        break

    # Knowledge base lookup
    elif user_input in knowledge_base:
        print("PyBot:", knowledge_base[user_input])

    # Fallback response
    else:
        print("PyBot: Sorry, I don't understand that. Please try another question.")
