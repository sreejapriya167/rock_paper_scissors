import random

rock = '''
     ______
---'      ____)
         (_____)
         (_____)
        (____)
---.__(__)
'''

paper = '''
     _____
---'   ____) _
          ______ ) 
          ________)
         _______)
---.______)
'''

scissors = '''
      _____
---'    ____) ____
          _________) 
           __________)
         (____)
---.__(___)
'''
choices= [rock,paper,scissors]
rules =[[ rock,scissors],
        [ scissors,paper],
        [ paper,rock]]
user_ch = input("Select one : 0 for rock, 1 for paper ,2 for scissors ? ").lower()
computer_ch= random.choice(choices)
if user_ch==0:
    print(f"User chose:{rock}")
elif user_ch ==1:
    print(f"User chose: {paper}")
else:
    print(f"User chose: {scissors}")

print(f"Compute chose:{computer_ch}")
if user_ch==computer_ch:
    print("--------Its a draw-------".upper())
elif [user_ch,computer_ch] in rules:
    print("--------Yay You win-------".upper())
else:
    print("--------Oops!You loose-----".upper())
