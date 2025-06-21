def motivation_for_u():
    import random
    import pyttsx3

    motivation = ["No one can fight your battles for you — not even the ones who love you the most. You have to stand, bleed, and rise on your own.",
                "Your biggest enemy is not out there — it's the version of you that refuses to change, to grow, to rise.",
                "The path to strength is walked alone — but a true friend will still walk beside you, even if they can't carry your weight.",
                "You can't heal in comfort — you heal by facing yourself, alone in the silence no one else can hear.",
                "Improve not for the world, not for applause — but because you owe it to the person staring back at you in the mirror.",
                "Your pain is your teacher, your struggle is your lesson — and only you can pass the test life gave you.",
                "Don't expect anyone to save you. That's your job. A real friend doesn't save you — they remind you that you can.",
                "Stop waiting for someone to understand you. Understand yourself. That's the start of real power.",
                "Loneliness teaches you the value of your own voice — and friends remind you it's worth being heard.",
                "Fight for your future like no one else will — because sometimes, no one else truly can."]

    def choice():
        return random.choice(motivation)

    def speak(data):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.say(data)
        engine.runAndWait()
        engine.stop()

    speak("Enter Your Name Warrior")
    Name = input("Enter Your Name Warrior: ").upper()

    def file(data):
        folder = "user_answer"
        fileName = folder + "/" + Name + "_motivate.txt"
        with open(fileName, "w") as f:
            f.write(f"{Name} Answer Is FOllowing >>>> \n\n")
            f.write(data)

    speak(f"\nwhat is your mood right now {Name} ?? Enter sad, tired, demotivated: ")
    mood = input(f"\nwhat is your mood right now {Name} ??\n Enter sad, tired, demotivated: \n").strip().lower()

    if mood == "sad" or mood == "tired" or mood == "demotivated":
        print(f"Why are You Felling {mood} ?? ")
        speak(f"Why are You Felling {mood} ?? ")
        speak(f"Give Answer {Name}:")
        speak("Type Here")

        ans = input(f"\nGive Answer {Name} \n \t Type Here:")
        file(ans)

        print("Don't worry, everything will be right after some time.\n")
        speak("Don't worry, everything will be right after some time.")
        print(f"Here Something Special For You, Dear {Name} \n")
        speak(f"Here Something Special For You, Dear {Name}")
        
        motivate = choice()
        print("Motivation For You: \n" + motivate)
        speak("Motivation For You")
        speak(motivate)
    else:
        print("Invalid Input⚠️⚠️")
        speak("Invalid Input")


if __name__ == "__main__":
    motivation_for_u()
