'''🔹 4. WhatsApp Auto Messenger (Advanced)
✅ What it does:
Automatically sends a message on WhatsApp Web to selected people.

📌 Features:

Opens WhatsApp Web

Searches contact

Types and sends the message

Uses pyautogui + time + clipboard

💡 Real Use: Use it for birthday wishes, reminders, or bulk alerts.'''



import pyautogui as pa
import time
import pyttsx3
import speech_recognition as sr
import os

r = sr.Recognizer()
def speak(data):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    engine.setProperty('rate',145)
    engine.setProperty('volume',1.0)

    engine.say(data)
    engine.runAndWait()
    engine.stop()
    
def get_voice(pro):
    try:
        with sr.Microphone() as source: 
            r.adjust_for_ambient_noise(source, duration=0.1)
            print("Listening...")
            speak("Listening...")
            audio = r.listen(source , phrase_time_limit = 120)
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I didn't understand.")
        return get_voice(pro)
    

speak("whom you want to send message boss!!")
contact =get_voice("listening......")

pa.hotkey('win')
time.sleep(1)
pa.write('whatsa')
time.sleep(1)
pa.press('enter')
time.sleep(3)  # give WhatsApp time to open
pa.write(contact)
time.sleep(1)
pa.press('enter')
time.sleep(1)
pa.press('down')
time.sleep(1)
pa.press('enter')

speak("what message you want to send boss!!")
message = get_voice("listening")

if message:
    pa.write(message)
    time.sleep(1)
    pa.press('enter')
    speak("message sent successful boss....")
    os.system("taskkill /f /im WhatsApp.exe")

else:
    speak("sorry boss messaege not send")
    os.system("taskkill /f /im WhatsApp.exe")
with open("message_log.txt", "a") as file:
    file.write(f"Sent to {contact}: {message}\n")
