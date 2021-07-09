# Stone ,Paper,Siccisor
import random

def game(comp,b):
    if comp == b:
        print("Tie!")
    if comp =="s":
        if b =="p":
            print("You Win!")
        elif b == "c":
            print("You Loss!")
    elif comp =="p":
        if b =="c":
            print("You Win!")
        elif b == "s":
            print("You Loss!")
    elif comp =="c":
        if b =="s":
            print("You Win!")
        elif b == "p":
            print("You Loss!")
            
print("Welcome lets play the game!!!!\n")
print("--------------------------------------")
print("Computer's Turn :\nChoose 's' for Stone\nChoose 'p' for Paper\nChoose 'c' for Siccisor")

randno = random.randint(1,3)
if randno == 1:
    comp ="s"
elif randno ==2:
    comp = "p"
elif randno ==3:
    comp ="c"
    
b = input("Your Turn :\nChoose 's' for Stone\nChoose 'p' for Paper\nChoose 'c' for Siccisor: ")

game(comp,b)

print(f"Computer choose '{comp}' and you choose'{b}'")
