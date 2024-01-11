import random 
a=input("Hello,Welcome to the dice game! To start enter your name.")
d=0
e=0
for i in range(6):
    b=random.randint(1,6)
    c=random.randint(1,6)
    if b>c:
            print("We roll the dice and!!! Looks like you won this round because",b," > ",c)
            d+=1
    elif c>b:
            print("We roll the dice and!!! Looks like I won this round because",c," > ",b)
            e+=1
    else:
            print("Its a draw!!",b," = ",c)
    if d==3:
            print("Looks like you won! Good job!")
    elif e==3:
            print("Looks like I won,Better luck next time!")
           





