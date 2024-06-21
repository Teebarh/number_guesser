# Guess The Number: Write a program where the computer randomly generates a number between 0 and 20. 
# The user needs to guess what the number is. 
# If the user guesses wrong, tell them their guess is either too high or too low. 

from random import randint

number = randint(0, 20)
print(number)
    

while True:
    prompt = int(input("Enter a number between 0 - 20: "))
    if prompt > number:
        print("Your guess is too high. Try again.")
    elif prompt < number:
        print("Your guess is too low. Try again.")
    elif prompt == number:
        print("You got it!")
        break
    