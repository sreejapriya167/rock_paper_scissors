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
choices= [rock,paper,scissors]
rules =[[ 0,2],
        [ 2, 1],
        [ 1, 0]]
user_ch = int(input("Select one : 0 for rock, 1 for paper ,2 for scissors ? "))
computer_ch= random.randint(0,2)


print(f"User chose:\n {choices[user_ch]}")

print(f"Compute chose:{choices[computer_ch]}")
if user_ch==computer_ch:
    print("--------Its a draw-------".upper())
elif [user_ch,computer_ch] in rules:
    print("--------Yay You win-------".upper())
else:
    print("--------Oops!You loose-----".upper())
