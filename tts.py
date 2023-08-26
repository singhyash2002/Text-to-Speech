import pyttsx3

engine = pyttsx3.init()

while True:
    answer = input("What you want to hear: \n")
    engine.setProperty('rate', 100)
    engine.say(answer)
    engine.runAndWait()
    engine.stop()
