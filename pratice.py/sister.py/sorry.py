import random
import pyttsx3
import pyjokes
def sisster():
    def speak(data):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.setProperty('rate', 140)
        engine.setProperty('volume',1.0)
        engine.say(data)
        engine.runAndWait()
        engine.stop()

    annoy = ["Sleeping Beauty" , "Chatterbox" , "Miss Always Right" , "Mood Swing Machine " , "Snack Stealer " ]
    data = ["Dear sister, I know the prank I played hurt you, and for that, I'm truly sorry. I thought it would be fun, but I forgot that sometimes laughter can hide pain. I never wanted to see you upset — you mean too much to me. You're not just a friend, you're like the sister my heart chose. If my joke broke your trust, I want to fix it with my honesty and love. Please forgive me, your silly brother who sometimes makes mistakes but never stops caring for you",
            "I know I crossed the line with my prank, and I regret it deeply. It was never my intention to hurt your feelings. You're one of the most precious people in my life — a sister not by blood, but by bond. I miss your smile, your laugh, and the warmth of our friendship. Please forgive me for being careless. Your happiness means more to me than any joke ever could.",
            "My dear sister, I'm sorry from the deepest corner of my heart. The prank was stupid, and I realize now that it wasn't funny — it was hurtful. I feel ashamed for turning a moment of joy into discomfort for you. I promise, from now on, my actions will always respect the love and care we share. Please forgive your emotional brother who just wants to see you smile again.",
            "I know I messed up, and it hurts knowing you're upset with me. You may not be my sister by blood, but in my heart, you're more than that. You're my strength, my safe place — and this brother of yours is truly sorry. Please forgive me."]

    def annoying():
        return random.choice(annoy)

    def sorry():
        return random.choice(data)

    anooy = annoying()
    taide = sorry()
    speak(f"Enter your name dear {anooy}. Type Here:")
    name = input(f"Enter your name dear {anooy} \n \t Type Here: ")

    def file(self):
        fileName = name.upper() +"_sis_replay.txt"
        with open(fileName, "a") as f:
            f.write(name + "\n")
            f.write(f"answer of dear {name}:\n\t"+ self + "\n\n\n")


    print("Hey, what happened? \n \t why Are you upset with me?")
    speak("Hey, what happened?")
    speak("why Are you upset with me?")
    question = f"Answer Me dear {anooy}"
    speak(question)
    speak("Type Here")
    ans = input(f"Answer Me dear {anooy} 😂\n \t Type Here:  ")

    file(ans)
    print(taide)
    speak(taide)

if __name__ == "__main__":
    sisster()
