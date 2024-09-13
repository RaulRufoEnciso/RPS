import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images =[rock, paper, scissors]

user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if (user_pick >= 3 or user_pick< 0):
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_pick])

    computer_pick = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_pick])

    if user_pick == 0 and computer_pick == 2:
        print("You win!")
    elif computer_pick == 0 and user_pick == 2:
        print("You lose!")
    elif computer_pick > user_pick:
        print("You lose")
    elif user_pick > computer_pick:
        print("You win")
    elif computer_pick == user_pick:
        print("It's a draw")

