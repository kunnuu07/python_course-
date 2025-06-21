import random
import pyttsx3

def dear_sis():
    def speak(data):
        engine = pyttsx3.init()

        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)

        engine.setProperty('rate',155)
        engine.setProperty('volume',1.0)
        engine.say(data)
        engine.runAndWait()
        engine.stop()

    annoying_words = ["Drama Queen","Miss Disturbance","chatterbox","Trouble Magnet","Mood Swing Machine","Crrying Queen"]
    motivational_lines = [
        "💪 As your brother, I've seen your strength, your kindness, and your heart. Don't ever let sadness make you forget who you are.",
        "🤗 Whenever you feel lost, remember your brother is right here — cheering for you, standing by you, and believing in you always.",
        "🔥 You're never alone in this world — you've got a brother who would walk through fire just to see you smile again.",
        "🕊️ Cry if you must, rest if you need — but promise me you won't give up. Your brother believes in you more than words can say.",
        "🛡️ No matter how grown-up we get, you'll always be my little sister — and I'll always protect your heart like it's my own.",
        "👣 We've shared laughter, dreams, and childhood — let's walk through the tough times too, hand in hand like we always have.",
        "🤲 You've always been the one who lifts others up. Now it's my turn — lean on me, sis. Your brother's got you.",
        "📍Remember who you are — bold, beautiful, kind, and unstoppable. Your brother sees it every day.",
        "📖 Sis, you've faced hard days before, and every time you've risen higher. This is just another chapter — and I'm here for every page.",
        "✨ You were born to shine. A sad day doesn't take away your light — it only makes it stronger. Your brother knows your true glow.",
        "🌍 No matter how lost you feel, your heart will always guide you home — and I'll always be there, your brother and your safe place.",
        "🧵 You're stitched with strength and hope — and your brother is here to hold the thread when you feel like you're unraveling.",
        "🎵 Even in silence, your soul sings. And I hear every note, loud and proud — that's what brothers do.",
        "💬 When your thoughts get heavy, let my words lift you. Your brother will always remind you how precious you are.",
        "🏠 No matter how far apart we are, you'll always have a safe place in my heart — your brother's heart."
    ]

    happy_lines = [
        "🌟 Your happiness is like sunshine — it brightens everyone around you!",
        "🎉 Keep that smile alive — it's your superpower!",
        "😊 Seeing you happy makes the world a better place.",
        "💫 You're glowing, and it's beautiful to witness!",
        "🎈 Life feels better when you're laughing like this!",
        "💖 Happiness looks so good on you — wear it every day!",
        "🌼 May your joy continue to bloom like a garden in spring!",
        "🥳 Keep shining and spreading those good vibes everywhere!",
        "🌈 When you're happy, it's like rainbows follow you around!",
        "✨ Your joy is contagious — never stop being this amazing!"
    ]

    brother = (
            " Remember, I'm not just your brother in sadness — "
            "I'm your biggest cheerleader in happiness too. "
            "Your joy means the world to me, and I'll always be right here, "
            "celebrating every smile, every success, and every laugh with you!"
        )
    def brother_emotions():
        print("\t" + brother)
        return speak(brother)

    def happy():
        happy_sis = random.choice(happy_lines)
        print(happy_sis)
        return speak(happy_sis)


    def get_random_quote():
        return  random.choice(motivational_lines)

    def Annoying():
        return  random.choice(annoying_words)
    annoy = Annoying()

    def save_file(name, ans):
        filename = name + ".txt"
        with open(filename, "w") as f:
            f.write(f"\nWhat happened, dear {name}? Why are you feeling sad?")
            f.write("\n\nThe Answer of User is as follows:\n\n")
            f.write(ans)

    def mood():
        name = input("Enter your name, dear: ")
        print(f"\nWhat is your mood right now, {name}?")
        mood_input = input("Type 'happy' or 'sad': ").strip().lower()

        if (mood_input == "sad"):
            print(f"\nWhat happened, dear {name}? Why are you feeling sad?")
            speak(f"\nWhat happened, dear {name}? Why are you feeling sad?")
            speak(f" Tell Me {annoy}")
            ans = input("Give me your answer: \n")
            save_file(name, ans)

            print("💌 Here's something to lift your spirits: \nDear Sis💕💕")

            printt = " Here's something to lift your spirits: Dear Sis"
            speak(printt)

            lines = get_random_quote()
            print(lines)

            brother = "Your Dear Brother Kunu"
            print("\t\t\t\t\t\t\t\t\t\t❤️ \"Your Dear Brother Kunu\" ❤️\n")

            speak(lines)
            speak(brother)

        elif (mood_input == "happy"):
            print(f"\n😄 That's good, my dear {name}. Keep smiling and spreading joy! 🌞\n")
            speak(f"That's good, my dear {name}. Keep smiling and spreading joy!")
            happy()
            print("Here are a special Message from your brother: \n")
            speak("Here are a special Message from your brother")
            brother_emotions()
        else:
            print("⚠️ Invalid input. Please type 'happy' or 'sad' only.")


    mood()

dear_sis()