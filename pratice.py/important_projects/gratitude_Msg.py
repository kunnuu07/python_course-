import random
import pyttsx3
from datetime import datetime

# Function to get the current date for filename
def get_filename():
    today = datetime.now()
    date = today.strftime("%d-%m-%Y")
    filename = f"memory_{date}.txt"
    return filename, date  # Return both filename and date as string

# Function to make the program speak
def speak(data):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Female voice
    engine.setProperty('rate', 155)            # Speed
    engine.setProperty('volume', 1.0)          # Volume
    engine.say(data)
    engine.runAndWait()
    engine.stop()

# Function to save the gratitude note to a file
def save_to_file(question, user_response, gratitude_msg, date_str):
    with open("gratitude.txt", "w") as f:
        f.write(f"{question}\n")
        f.write(f"User's Answer: {user_response}\n")
        f.write(f"Gratitude Message: {gratitude_msg}\n")
        f.write(f"Date: {date_str}\n")

# List of gratitude messages
gratitude_quotes = [
    "Gratitude turns what we have into enough.",
    "Every small thing you appreciate today adds joy to your tomorrow.",
    "Thankfulness is the beginning of happiness.",
    "A grateful heart is a magnet for miracles.",
    "When you focus on the good, the good gets better.",
    "Each moment of gratitude plants a seed of peace in your heart.",
    "Gratitude doesn't change the situation, it changes your mindset — and that changes everything.",
    "Appreciate the little things; they often make the biggest difference.",
    "Being grateful for today builds strength for tomorrow.",
    "Your gratitude is a gift — to yourself and to the world around you."
]

# Function to choose a random gratitude quote
def get_gratitude_message():
    return random.choice(gratitude_quotes)

# Program starts here
question = "🌼 What are you grateful for today?"
print(question)
speak(question)

user_response = input("Enter your answer: \n\t")

gratitude_msg = get_gratitude_message()
print("\n💬 Gratitude Message:")
print(gratitude_msg)
speak(gratitude_msg)

filename, date_str = get_filename()

# Save the entry
save_to_file(question, user_response, gratitude_msg, date_str)

print(f"\n📝 Your gratitude has been saved in 'gratitude.txt'.")
speak("Your gratitude has been saved. Have a peaceful day.")
