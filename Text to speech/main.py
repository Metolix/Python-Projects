import pyttsx3

while True:

    line = input("What do you want the AI to say? ")
     
    if line == "quit":
        print("Quiting the program. Bye!")
        break
    else:
        engine = pyttsx3.init()
        engine.say(line)




        engine.runAndWait()