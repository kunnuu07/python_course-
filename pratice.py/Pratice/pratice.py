
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

engine.setProperty('rate',160)
engine.setProperty('volume',1.0)
engine.say("🏠 No matter how far apart we are, you'll always have a safe place in my heart — a place where you're never alone.")
engine.runAndWait()
engine.stop()




