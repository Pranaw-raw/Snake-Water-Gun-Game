import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you = youDict[youstr]

# By now we have 2 numbers (variables) computer and you. we have to compare them and decide the winner.

print(f"Computer chose {reverseDict[computer]}")
print(f"You chose {reverseDict[you]}")
if (computer == you):
    print("It's a tie!")

else:
    if (computer == -1 and you == 1):
        print("You win! ")
    elif (computer == -1 and you == 0):
        print("computer wins! ")
    elif(computer == 1 and you == -1):
        print("computer wins!")
    elif (computer == 1 and you == 0):
        print("You win.")         
    elif(computer == 0 and you == -1):
        print("You win! .")
    elif (computer == 0 and you == 1):
        print("computer wins!") 
    else:
        print("something went wrong! please try again.")