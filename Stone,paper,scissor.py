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
def ComputerChoices():
    ComputerChoices=["stone","paper","scissor"]
    getComputerChoices=random.choice(ComputerChoices)
    print(f"computer choice:{getComputerChoices}")
    return getComputerChoices
def userchoices():
    userchoices=input("user Choice!:").lower()
    return userchoices

def gameRule(PlayUser,PlayComputer):
    #draw match
    if PlayUser==PlayComputer:
        print("match Draw")
    #user wins
    elif(PlayUser=="paper" and PlayComputer=="scissor"):
        print("Computer wins")
    elif(PlayUser=="scissor" and PlayComputer=="stone"):
        print("Computer wins")
    elif(PlayUser=="stone" and PlayComputer=="paper"):
        print("Computer wins")
   
    elif(PlayUser=="paper" and PlayComputer=="stone"):
        print("user wins")
    elif(PlayUser=="scissor" and PlayComputer=="paper"):
        print("user wins")
    elif(PlayUser=="stone" and PlayComputer=="scissor"):
        print("user wins")
    
gameRule(PlayUser=userchoices(),PlayComputer=ComputerChoices())