# 🤖 Decode Labs – Rule-Based AI Chatbot (PyBot)

## 📌 Project Overview

PyBot is a simple **Rule-Based AI Chatbot** developed using Python as part of an Artificial Intelligence internship project at **Decode Labs**.

This chatbot interacts with users through the terminal and provides predefined responses to different messages using conditional statements (`if`, `elif`, and `else`).

The main goal of this project is to understand the fundamentals of chatbot development, input handling, and rule-based conversational logic.

## 🎯 Project Objectives

- Understand the basics of Artificial Intelligence.
- Develop a simple rule-based chatbot using Python.
- Implement user input handling and response generation.
- Use conditional statements for decision-making.
- Create a continuous conversation loop.
- Handle greetings, basic questions, and exit commands.

## ✨ Features

- 👋 **Greeting Responses:** Responds to Hello, Hi, Hey, and other greetings.
- 🤖 **Chatbot Identity:** Introduces itself as PyBot.
- 🧠 **AI Knowledge:** Provides a basic explanation of Artificial Intelligence.
- 💬 **Basic Conversations:** Responds to predefined questions.
- 🙏 **Thank-You Responses:** Replies politely to thank-you messages.
- 🚪 **Exit Commands:** Supports Bye, Exit, Quit, and Goodbye.
- 🔄 **Continuous Conversation:** Keeps interacting until the user exits.
- 🛡️ **Input Handling:** Removes unnecessary whitespace, converts input to lowercase, and handles empty messages.
- ❓ **Fallback Responses:** Handles unknown messages with a helpful suggestion.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Concepts:** Rule-Based Logic, Conditional Statements, Loops, String Manipulation, User Input Handling
- **Interface:** Command-Line Interface (CLI)

## 📂 Project Structure

```text
Decode-Labs-Rule-Based-Chatbot/
│
├── chatbot.py       # Main Python chatbot program
├── README.md        # Project documentation
```

## 💻 Example Output

```text
============================================================
        WELCOME TO DECODE LABS RULE-BASED AI CHATBOT
============================================================
Hello! I am PyBot, your simple rule-based AI assistant.
You can chat with me, ask questions, or type 'exit' to quit.
------------------------------------------------------------

You: Hello
Chatbot: Hello there! How can I assist you today?

You: What is your name?
Chatbot: I am PyBot, a rule-based AI chatbot created for Decode Labs.

You: What is AI?
Chatbot: Artificial Intelligence (AI) is the simulation of
human intelligence by machines to perform tasks like learning,
reasoning, and problem-solving.

You: Thanks
Chatbot: You're very welcome! Always happy to help.

You: Exit
------------------------------------------------------------
Chatbot: Goodbye! Have a wonderful day ahead!
============================================================
```

## 🧠 How It Works

The chatbot follows a simple rule-based approach:

1. Takes input from the user.
2. Removes extra spaces and converts the input into lowercase.
3. Removes trailing punctuation for flexible message matching.
4. Checks the user's message against predefined conditions.
5. Displays the corresponding response.
6. Continues the conversation until an exit command is entered.
7. Displays a fallback response if the input does not match any predefined rule.

## 🚀 Future Improvements

- Add more predefined questions and responses.
- Implement Natural Language Processing (NLP).
- Integrate a graphical user interface (GUI).
- Add voice input and output functionality.
- Store conversation history.
- Use machine learning to improve response generation.

## 👨‍💻 Author

**Developed as part of the Artificial Intelligence Internship at Decode Labs.**

## 📜 License

This project is created for educational and learning purposes. You are welcome to explore and modify the code for personal learning.

---

⭐ **If you like this project, don't forget to give it a star on GitHub!**

*Made with Python 🐍 and curiosity for Artificial Intelligence.*