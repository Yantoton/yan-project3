import time
import os
text ="""It's Time To Sleep
Eat
Sleep
Code
Repeat"""
emoji_translate ={
      "E":"🍕",
      "S":"🛌🏻",
      "C":"💻",
      "R":"🔁"
}
dict = text.maketrans(emoji_translate)
print(text.translate(dict))
for char in dict:
      print(char, end='')
      print("PC_System Will Sleep in 10 seconds>>...")
      time.sleep(0.3)
time.sleep(10)
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0.")
