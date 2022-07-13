import random
guess_taken=0
name=input("Hello! Enter you name:")
sys_limit_num=random.randint(0,10)
sys_guess=int(input(name+"I am gussed a number between 1 to 10,can u guess it?"))
while guess_taken<2:
    if sys_guess<sys_limit_num:
        print("you need to guess higher...Try again!")
        sys_guess=int(input("guess a number between 1 and 10:"))
    else:
        print("you need to guess lower... Try again!")
        sys_guess=int(input("guess number between 1 to 10:"))
    if sys_guess==sys_limit_num:
        break
if sys_guess==sys_limit_num:
    guess_taken=str(guess_taken)
    print("Good job!"+name+"you are guessed my number in"+guess_taken+"guesses")


if sys_guess!=sys_limit_num:
    num=str(num)
    print("nope,The nuber i was thinking",num)
    
