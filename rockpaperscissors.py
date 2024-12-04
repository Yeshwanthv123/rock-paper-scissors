import random
rock='''

    _______
---'   (____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps=[rock,paper,scissors]
uc=int(input("enter 0 for rock 1 for paper and 2 for scissor: "))
print(rps[uc])
x=random.randint(0,2)
print("the computer's choice is")
print(rps[x])
print(f"Computer choice is: {x}")
if uc==0 and x==2:
    print("you win")
elif x==0 and uc==2:
    print("you lose")
elif x>uc:
    print("you lose")
elif uc>x:
    print("you win")
else:
    print("draw")


