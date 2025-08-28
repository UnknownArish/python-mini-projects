
# This is a simple rule-based chatbot.

def get_response(user_input):
    """
    Returns a response based on the user's input.
    """
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    # Respond to greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # Respond to asking about the bot
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"

    # Respond to asking the bot's name
    elif "your name" in user_input:
        return "I'm a simple chatbot created in Python."

    # Respond to exit commands
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a nice day!"

    # Default response for unknown input
    else:
        return "Sorry, I don't understand that. Can you ask something else?"

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to the Simple Chatbot! (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower() or "exit" in user_input.lower() or "quit" in user_input.lower():
            break

if __name__ == "__main__":
    main()