from gtts import gTTS
import os

text = "चल रो मत बंदरिया, तेरा भाई खड़ा है तेरे साथ"
tts = gTTS(text=text, lang='hi')
tts.save("output.mp3")

# Play the mp3 file (works on Windows)
os.system("start output.mp3")
