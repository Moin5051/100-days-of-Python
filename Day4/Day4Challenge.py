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
game = [rock,paper,scissors]
print("Welcome to a simple Rock, Paper, Scissors Game")
x = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors \n"))
comp_choice = random.randint(0,2)


if x >=3 or x<0:
    print("That is an invalid number.")
else:
    print(f"You chose: {game[x]}")
    print(f"Computer chose: {game[comp_choice]}")

if x >= 3 or x <0:
    print("Choose between 0,1 and 2! Dont worry I can wait")
elif x == 0 and comp_choice ==2:
    print(" You win!!!")
elif comp_choice == 0 and x == 2 :
    print("You Loose!!! Womp Womp....")
elif comp_choice > x:
    print("You Loose!!! Womp Womp....")
elif x > comp_choice:
    print("You win!!")
elif x == comp_choice:
    print("It's a Draw, Try Again.")
