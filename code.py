import random
choices = {0: "Rock", 1: "Paper", 2: "Scissors"}
user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors."))
computer_choice = random.randint(0, 2)
print("Computer Chose: {}".format(choices[computer_choice]))
if computer_choice == user_choice:
    print("It's a draw.")
elif (computer_choice == 0 and user_choice == 2) or (user_choice == 1 and computer_choice == 0) or (
        user_choice == 2 and computer_choice == 1):
    print("You Lose.")
else:
    print("You Win.")
