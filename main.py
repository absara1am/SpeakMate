import pyttsx3

if __name__ == '__main__':
    while(True):
        print("Welcome to SpeakMate 1.1 Created by Absar")
        x = input("Enter what you want me to speak: ")
        engine = pyttsx3.init()
        if(x == "/"):
            break
        engine.say(x)
        engine.runAndWait()