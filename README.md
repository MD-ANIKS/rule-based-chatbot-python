# AI Study Buddy (Rule-Based Chat Assistant)

A lightweight, terminal-based conversational AI assistant built entirely with core Python logic. This chatbot greets users based on the time of day and intelligently matches user queries against a predefined memory bank using string manipulation and loops.

---

## 🎯 Project Objective
The goal of this project is to build a functional, mini AI chatbot assistant using pure Python fundamentals—including dictionaries, custom functions, string methods, `while` loops, and the `datetime` library. It simulates intelligent behavior through rule-based logic without relying on heavy external machine learning models.

---

## ✨ Features
*   **Time-Aware Greetings:** Dynamically greets the user with "Good Morning", "Good Noon", "Good Afternoon", "Good Evening", or "Good Night" depending on the system's current hour.
*   **Case-Insensitive Matching:** Converts user inputs and memory keys to lowercase on the fly to prevent matching errors (e.g., "WHO ARE YOU" will match "Who are you?").
*   **Sub-string Detection:** Uses the `in` operator so that keywords inside longer sentences are still recognized (e.g., typing *"please hello"* still triggers the hello response).
*   **Continuous Conversation:** Runs inside an interactive infinite `while` loop until explicitly closed.
*   **Graceful Exit:** Automatically breaks the loop and closes down when the user types "bye".

---

## 🛠️ Tech Stack & Concepts Used
*   **Language:** Python 3
*   **Modules:** `datetime` (for fetching system time)
*   **Data Structures:** Dictionaries (used as the chatbot's memory storage)
*   **Control Flow:** `if-elif-else` conditional states, `for` loops, and `while` loops
*   **String Manipulation:** `.lower()` method for robust pattern matching

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your computer. You can download it from [python.org](https://python.org).

### Installation & Running the Bot
1. Clone or download this project repository.
2. Create a file named `main.py` and paste the script code inside it.
3. Open your terminal or command prompt, navigate to the folder, and run:
   ```bash
   python main.py
   ```

---

## 💻 Sample Interaction
```text
Enter Your Name: Anik
Hey Anik Good Night!
Welcome Anik to Your Buddy ChatBot
You can ask me basic question, Type 'bye' to exit from the bot

Please ask your question: WHO ARE YOU?
Bot Response : I'm your freindly AI Study Buddy created by Md.Anik

Please ask your question: Can you motivate me please?
Bot Response : Keep going! Every bug you fix makes you a better coder

Please ask your question: goodbye!
Bot Response : Thanks for using Chatboat!
```

---

## 🧠 Core Logic Explained

### 1. The Double Datetime Trick
The script uses `datetime.datetime.now().hour`. Here is how it reads:
*   The first `datetime` targets the imported **library module**.
*   The second `datetime` targets the specific **class tool** inside that library.
*   `.now().hour` fetches the current hour index integers (`0` through `23`).

### 2. Case-Insensitive Memory Matching
To avoid issues where uppercase inputs fail dictionary lookups, the search logic performs structural comparison in lowercase without editing the database:
```python
for eachKey in responses:
    lowerCaseKey = eachKey.lower() # Temporary lowercase holder
    if lowerCaseKey in userInput:
        return responses[eachKey] # Fetches item using the original unchanged key
```

---

## 👨‍💻 Author
Created with 💻 by **Md. Anik**. 
