# word = "amazing"
# k = word[1:6:2]
# print(k)

# k = 'kunnu'
# print(k.find("u"))

# n = [1,2,2,2,2,3,4,5,6,7]

# num = n.count(2)
# for i in range(num):
#     n.remove(2)
# print(n)

import pywhatkit as kit
import wikipedia as wi

audio = {"husn": 'https://www.youtube.com/watch?v=gJLVTKhTnog&list=RDgJLVTKhTnog&start_radio=1'}
play = audio.get("husn")
wi.summary(play)
# kit.playonyt(play)
