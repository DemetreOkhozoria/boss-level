z=input("Create new account or Log in?")
if z == "Create new account":

    input("Enter your name!")
    input("Enter your surname!")
    input("enter your username!")
    input("Enter your Email address!")
    input("Enter your card number!")
    input("Enter your password!")

elif z=="log in":
    input("Enter your username!")
    input("Enter your password!")


else: print("that's an error") 

if z=="log in" or z=="Create new account":

    b=input("Do you wanna deposit or withdraw your money?")

    money=1000

    if b==("Deposit"):

        c=input("How much do you want deposit?")
        print("On card You now have " ,(int(c)+int(money)))

    elif b==("Withdraw"):
        c=input("How much do you want Withdraw?")
        if int(c)>1000:
            print("that's an error")
        else:
            print("On card you now have " ,(int(money)-int(c)))