import pyttsx3

if __name__=='__main__':
    print("Welcome to robo speaker")
    engine=pyttsx3.init()
    while(True):
        x = input("What you want to say?")
        if(x=='EXIT' or x=="exit"):
            break
        else:
            engine.say(x)
            engine.runAndWait()