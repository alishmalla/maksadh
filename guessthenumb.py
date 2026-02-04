# import random

# randnum = random.randint(1, 50)
# print("Let me guess a number from 1 to 50")

# while True:
#     try:
#         intnum = int(input("Guess a number from 1 to 50: "))
#         if randnum > intnum:
#             print("The number is too low. Guess again.")
#         elif randnum < intnum:
#             print("The number is too high. Guess again.")
#         else:
#             print("Your guess is correct!")
#             break
#     except ValueError:
#         print("Please enter a valid integer.")



# import random
# randnum= random.randint(1,51)
# print("Welcome to the guessing game /nI will think of a number and you guess it. Simple!")
# mode=str(input('Choose the mode you want to play in easy or hard?/nE= 10 chances, H= 5 chances '))
# if mode== 'E':
#     chances=10
# elif mode=="H":
#     chances=5
# else:
#     print('Error. Selecting Easy mode!')
#     chances=10

# while chances>0:
    
#       guess=int(input("Guess a number "))
#       if guess>randnum:
#           print('Too high!')
#       elif guess<randnum:
#           print("Too low!")
#       else:
#           print("Correct🙌")
#       break 
#       chances-=1
#       if chances<0:
#           print(f"You've {chances} chances left")
#       else: print("You're out of chance ")



import random

randnum = random.randint(1, 50)
print("Welcome to the guessing game!")
print("I will think of a number and you guess it. Simple!")

mode = input("Choose the mode you want to play in (Easy or Hard):\nE = 10 chances, H = 5 chances\n").upper()

if mode == 'E':
    chances = 10
elif mode == 'H':
    chances = 5
else:
    print("Invalid choice. Defaulting to Easy mode.")
    chances = 10

while chances > 0:
    guess_input = input("Guess a number: ")
    
    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess_input)

    if guess > randnum:
        print("Too high!")
    elif guess < randnum:
        print("Too low!")
    else:
        print("Correct 👏👏")
        break

    chances -= 1
    if chances > 0:
        print(f"You have {chances} chances left.")
    else:
        print(f"You're out of chances! The number was {randnum}.")


        
    
