import pyttsx3

def speak(data):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    engine.setProperty('rate',130)
    engine.setProperty('volume',0.9)
    engine.say(data)
    engine.runAndWait()
    engine.stop()

def file():
    with open("database_file.txt") as f:
        read = f.read()
        return read 
    
speak(file())