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
options = [rock,paper,scissors]
while True:
  User = int(input("0 -> Rock , 1 -> paper , 2 -> scissors\n enter your choice: "))
  comp= random.randint(0,2)
  print("you chose: ",options[User])
  print("Comp chose: ",options[comp])
#game
  if User==comp:
    print("It's a draw ^^")
  elif (User==0 and comp==2) or (User==1 and comp==0) or(User==2 and comp==1):
    print("YAY !! you won ")
  else:
    print("oh! you lost :(")
"""
options =[rock,paper,scissors]
while True:
 User=int(input("enter your choice))
 comp=random.randint(o,2)
 print('u chose',options[User])
 print('we chose',options[comp])
 if User==comp:
 print('draw')
 elif(user>comp):
 print(you won0)
 else:
 print(u lost)
 
 """
