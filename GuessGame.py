import random

target = random.randint(1, 100)

while True:
    userchoice = int(input("Guess The Target or Quit(Q): "))
    if userchoice == "Q" :
        break

    if (userchoice == target):
        print("Success!!! Correct Guess 🎉")
        break  # Break should be inside the correct condition

    elif userchoice < target:
        print("Your number was too small, try a bigger one.")

    else:  # No need to check if it's greater, it's the only remaining possibility
        print("Your number was too big, try a smaller one.")

     