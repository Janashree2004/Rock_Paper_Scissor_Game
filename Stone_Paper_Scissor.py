import random
rock='''
         _______
_______/    _____)
            (_____)
            (______)
______      (_____)
      \_____(___)
'''

paper='''
           ________
_________/        __)_____
                  (________)
                  (_________)
______            (________)
      \___________(_______)
'''

scissor='''
           ____
_________/    __)_______
            (____________)
            (_____________)
______      (_____)
      \_____(___)
'''
n=[rock,paper,scissor]
a=int(input("Enter the choice:- Type 0 for Rock, 1 for paper, 2 for scissor: "))
if a>3 or a<0:
    print("Invalid user, You Lose.")
else:
    print(n[a])
    b=random.randint(0,2)
    print("Computer choice:")
    print(n[b])
    if a==b:
        print("It's A draw.")
    elif a==0 and b==2:
        print("You Lose.")
    elif a==2 and b==0:
        print("You Win.")
    elif a>b:
        print("You Lose.")
    elif a<b:
        print("You Win.")
