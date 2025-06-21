import random
import pyttsx3 as bolo


engine = bolo.init()
def speak(data):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',155)
    engine.setProperty('volume',1.0)
    engine.say(data)
    engine.runAndWait()
    engine.stop()

speak("enter your name ")
user = input("enter your name : ")
speak("Enter Your first love name ")
lover = input("Enter Your first love name: ")
def file(data):
    filename = user + "_lover_ans.txt"
    with open(filename , "a") as f:
        f.write(f"lover name of {user} is : "+lover)
        f.write("\nlover expections or thinking about her/him:\t"+data)



print("your first love in your life say [yes]. or [cheated,one side , she/he not intrested in you or rejected you]")
speak("your first love in your life. say yes! or cheated or one side or she or he not intrested in you or rejected you")
speak("\t enter here:")
ans = input("\t enter here:")


if "cheated" in ans.lower() or any(w in ans.lower() for w in ["cheated", "one side" , "she/he not intrested in you", "rejected you"]):
    print('\nsuppose Your crush or first love propose you. what think you say him/her??')
    speak('suppose Your crush or first love propose you. what think you say him or her??')
    
    speak(f"\n \tgive me answer dear lover {user}:")
    print(f"\n \tgive me answer dear lover {user}:")
    
    speak(f"type here {user}:")
    answer = input(f"\n \t type here {user}:")
    file(answer)
    print("ok don't be sad, forgot the past and live in present now😔")
    speak("ok don't be sad, forgot the past and live in present now")

else:
    print(f"ok good job dear {user}. stay loyal with her/him...👍")
    speak(f"ok good job dear {user}. stay loyal with her or him...")
    
