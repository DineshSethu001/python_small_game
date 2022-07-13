# Thinks to know
#     *Random Module
#     *Function
#     *User Input
#     *Condition _Statement

# game Working:
#     -Computer choice
#     -User choice
#     -game rule

import random
def computer():
    computerChoice=["rock","paper","scissor"]
    getComputerChoice=random.choice(computerChoice)
    print(f"The computer choice is:{getComputerChoice}")

    return getComputerChoice


def user():
    userChoice=input("Enter any from below one:\n 1.Rock\n 2.Paper\n 3.Scissor\n here:").lower()
    return userChoice
def gameRule(userchoice,sys_choice):
    #draw
    if userchoice==sys_choice:
        print("Match Draw")
  
  
    elif(userchoice=="scissor" and sys_choice=="paper"):
        print("user wins")
   
    elif(userchoice=="stone" and sys_choice=="scissor"):
        print("user Wins")
    elif(userchoice=="rock" and sys_choice=="scissor"):
        print("user wins")

    elif(userchoice=="rock" and sys_choice=="paper"):
        print("system wins")
   
    elif(userchoice=="scissor" and sys_choice=="rock"):
        print("system wins")
    elif(userchoice=="paper" and sys_choice=="scissor"):
        print("System wins")
    

gameRule(userchoice=user(),sys_choice=computer())
