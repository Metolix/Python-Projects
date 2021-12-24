import pyttsx3

while True:

    line = input("What do you want the AI to say?(Tip - If you want the bot to quit, say 'quit') ")
     
    if line == "quit":
        print("Quiting the program. Bye!")
        break
    else:
        engine = pyttsx3.init()
        engine.say(line)




        engine.runAndWait()