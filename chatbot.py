def chatbot():
    """Main function to run the Rule-Based AI Chatbot."""
    # 1. Welcome Message & Clean Terminal Interface
    print("=" * 60)
    print("        WELCOME TO DECODE LABS RULE-BASED AI CHATBOT        ")
    print("=" * 60)
    print("Hello! I am PyBot, your simple rule-based AI assistant.")
    print("You can chat with me, ask questions, or type 'exit' to quit.")
    print("-" * 60)

    # 6. Continuous Conversation Loop
    while True:
        # Prompt the user for input
        raw_input = input("\nYou: ")

        # 8. Input Handling: Strip whitespace and convert to lowercase
        user_input = raw_input.strip().lower()
        
        # Clean trailing punctuation (? ! . ,) for flexible matching
        normalized_input = user_input.rstrip("?!.,")

        # 10. Empty Input Handling
        if user_input == "":
            print("Chatbot: It looks like you didn't type anything. Please enter a message!")
            continue

        # 5. Exit Commands & Loop Termination
        if normalized_input in ["bye", "exit", "quit", "goodbye"]:
            print("-" * 60)
            print("Chatbot: Goodbye! Have a wonderful day ahead!")
            print("=" * 60)
            break

        # 2. Greeting Responses
        elif normalized_input in ["hello", "hi", "hey", "good morning", "good evening"]:
            print("Chatbot: Hello there! How can I assist you today?")

        # 3. Basic Conversation: Predefined Questions
        elif normalized_input in ["what is your name", "who are you"]:
            print("Chatbot: I am PyBot, a rule-based AI chatbot created for Decode Labs.")

        elif normalized_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm just a computer program, but I'm functioning smoothly! How are you doing?")
            
        elif normalized_input in ["what is ai", "what is artificial intelligence"]:
            print("Chatbot: Artificial Intelligence (AI) is the simulation of human intelligence by machines to perform tasks like learning, reasoning, and problem-solving.")

        elif normalized_input in ["what can you do", "what are your features"]:
            print("Chatbot: I can greet you, answer basic questions about myself and AI, respond to thank-you messages, and chat using rule-based logic.")

        elif normalized_input in ["what is your purpose", "why were you created"]:
            print("Chatbot: My purpose is to demonstrate rule-based conversational logic for an Artificial Intelligence internship project at Decode Labs.")

        # 4. Thank-You Responses
        elif normalized_input in ["thanks", "thank you", "thank you very much"]:
            print("Chatbot: You're very welcome! Always happy to help.")

        # 9. Unknown Inputs / Fallback Response
        else:
            print("Chatbot: I'm sorry, I don't understand that yet. I am a rule-based chatbot with predefined responses.")
            print("         Try asking: 'What is your name?', 'What is AI?', 'What can you do?', or say 'hello'.")


# 12. Code Structure: Program entry point
if __name__ == "__main__":
    chatbot()
