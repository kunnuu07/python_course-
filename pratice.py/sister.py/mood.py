import pyttsx3

def say(self):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',140)
    engine.setProperty('volume',1.0)
    engine.say(self)
    engine.runAndWait()
    engine.stop()

def mood():
    def save_file(name , ans):
        filename = name + ".txt"
        with open(filename, "w") as f:
            f.write("The Answer of User Is Following>>>>> \n\n")
            f.write(ans)

    say("Enter Your Name Dear")
    name = input("Enter Your Name Dear: ")
    

    say(f"What Is Your Mood Right Now Dear {name} . Happy or Sad??? ")
    print(f"\nWhat Is Your Mood Right Now Dear {name}.Happy or Sad??? ")
    say("Type here")
    mood = input(f"\t Type here: ")

    mood.lower()

    if (mood == "sad"):
        say(f"What Happend Dear {name} Why are you Felling Sad")
        print(f"What Happend Dear {name} Why are you Felling Sad")
        say("Give Me Answer ")
        ans = input("\t Give Me Answer: ")
        save_file(name,ans)
        say(f"Don't Worry, Dear {name}. Everything will be right. Just forget the past and Keep Smiling")
        print(f"\nDon't Worry, Dear {name}. Everything will be right. \n Just forget the past and Keep Smiling")

    elif (mood == "happy"):
        say(f"That's Good My Dear {name} Keep Smiling")
        print(f"\nThat's Good My Dear {name} \n Keep Smiling")

    else:
        say(f"Invalid Input!!!")
        print(f"\nInvalid Input!!!")



mood()