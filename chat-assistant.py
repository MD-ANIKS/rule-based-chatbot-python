# Learning Project - AI Studty Buddy (Rule-Based Chat Assistant in Python)

import datetime
import time

name = input("Enter Your Name: ")
presentHour = datetime.datetime.now().hour

if 4 <= presentHour <= 12:
  print(f"Hey {name} Good Morning!")
elif 1 <= presentHour <= 3:
  print(f"Hey {name} Good Noon!")
elif 3 < presentHour <= 5:
  print(f"Hey {name} Good AfterNoon!")
elif 5 < presentHour <= 7:
  print(f"Hey {name} Good Evining!")
else :
  print(f"Hey {name} Good Night!")

print(f"Welcome {name} to Your Buddy ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [Form of dictionary type responses]

responses   = {

  "hello": "Hi there! How can I help you today?",
  "Who are you?": "I'm your freindly AI Study Buddy created by Md.Anik",
  "Motivated me": "Keep going! Every bug you fix makes you a better coder",
  "happy": "Great to hear that",
  "bye": "Thanks for using Chatboat!"
}

# create a getResponseOfBot method/function to get response of chatbot
def getResponseOfBot(userInput):
    userInput = userInput.lower()
    for eachKey in responses:
      lowerCaseKey = eachKey.lower()
      if lowerCaseKey in userInput:
        return responses[eachKey]
    return "I'm not able to tell that yet, Still Learning! "

while True:
  # take user input
  userInput = input("Please ask your question: ")
  reply = getResponseOfBot(userInput)
  print("Bot Response :",  reply)

  if "bye" in userInput.lower():
    break

