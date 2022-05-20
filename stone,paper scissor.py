import random
from tkinter.messagebox import NO

def gamewin(comp,you):
    if comp == "Stone":
        if you == "Paper":
            return True
        elif you == "Scissor":
            return False
        else:
            return None
    if comp == "Paper":
        if you == "Scissor":
            return True
        elif you == "Stone":
            return False
        else:
            return None
    if comp == "Scissor":
        if you == "Stone":
            return True
        elif you == "Paper":
            return False
        else:
            return None

    
list=["Stone","Paper","Scissor"]
print("Comp turn: Stone, Paper or scissor.")
comp=list[random.randint(0,2)]

a=int(input("Your turn: Stone(1), Paper(2) or Scissor(3) :: "))
you=list[a]


print(f"Computer Selected {comp}")
print(f"You Selected {you}")

b=gamewin(comp,you)

if b== None:
    print("It's a Tie")
elif b:
    print("You Won")
else:
    print("You Lost")







