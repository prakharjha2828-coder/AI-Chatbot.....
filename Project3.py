#Mini AI Chatbot
import datetime
import time 
Name = input("Swagat h ji, enter your name :")
persentHour = datetime.datetime.now().hour
if 5 <= persentHour <= 11:
    print("Good Morning!",Name)
elif 12 <= persentHour <= 17:
   print("Good after Noon!",Name)
elif 17 <= persentHour <= 21:
    print("Good eveing!",Name)
else:
    print("Good night!",Name)

print("Namaste Welcome to rule base chatbot")
print("you can ask mein basic question ,type 'bye' to exit from the bot")

#chatbot memory Creation[Distionary of responses]

responses = {
    "Hello": "HI, How can you can I help me?",
    "How are you": "I am very fine.",
    "Who are you": " I am smart AI chatbox.",
    "Motivate Me":"keep goging every bug of your project makes you a better devloper best.",
    "Happy": "solve all problem beacuse your mind is happy.",
    "Function kay hote h ji": "Google kro ji.",
    "Hindi kay h ji": "Hindi ek language h ji to india , neple , pakisatn , bengaladesh mein boli jati h ji.",

}

#Method/function to get response of chatBot

def getResponseOfBot(userQusetion):
    userQusetion = userQusetion.lower()
    for eachkey in responses:
        if eachkey .lower() in userQusetion:
            return responses[eachkey]
    return "Abhi mujhe wo nahi ate h ji,sorry. Abhi learning mode mein hu ji."

#take user input
while True: 
    userinput = input("Please ask your question.")
    reply = getResponseOfBot(userinput)
    print("Bot Response :", reply)
    if "bye" in userinput.lower():
        break


