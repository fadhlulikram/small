import random

Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

rps = [Rock, Paper, Scissors]

compt = random.randint(0, 2)

dummy = [2, 0, 1]
if dummy[user] == compt:
    print(user)
    print(compt)
    print(f"You choose {rps[user]}\n\nComputer choose{rps[compt]}\n\nYou Win")
elif user == compt:
    print(user)
    print(compt)
    print(f"You choose {rps[user]}\n\nComputer choose{rps[compt]}\n\nYou Draw")
    
else:
    print(user)
    print(compt)
    print(f"You choose {rps[user]}\n\nComputer choose{rps[compt]}\n\nYou Lose")
    

