import random

'''
1 for snake
-1 for water
0 for gun
'''


computer = random.choice([1,0, -1])
youstr = input("enter your choice: ")
Dict={"s":1, "w": -1, "g": 0 }
reverseDict = {1:"Snake", -1 :"Water", 0:"Gun"}


you = Dict[youstr]

print(f"Computer chosed {reverseDict[computer]} and You chosed {reverseDict[you]}")
if ( computer==you): 
    print("It is a draw")
else:
    if (computer- you==-1) or (computer- you==1) or (computer - you ==2):

        print ("You lose")
    else:
      print("You win")