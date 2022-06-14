# Rock Paper Scissor Game
import random          # Importing random module 
lst = ["r", "p", "s"]  # Making a lsit for picking random word from computer side

a = input("Enter your name")    # asking user's name to making it feel real

chance = 5           # Total number of chance
no_of_chance = 0
computer_point = 0
a_point = 0

print("\t\t\t\tRock,Paper,Scissor Game")
print("\t\t\t\tBest of 5 will be Winner")

print("r for Rock \np for Paper\ns for Scissor\n")

while no_of_chance<chance:
    print("\n\t\t------ TURN ", str(no_of_chance + 1), " ------")
    _input = input("Rock,Paper,Scissor:")         # Taking input from user 
    _random = random.choice(lst)                  # Taking input from computer using random module       
    no_of_chance +=1      
    if _input == _random:
        print("Both of you chose the same")
        print("It's a Tie\n")

    elif _input == "s" and _random == "r":
        computer_point += 1
        print(f"You chose {_input} and computer chose {_random}\n")                        # showing inputs of both
        print("computer gets 1 point\n")                                                   # increasing a point in the winner's side         
        print(f"computer point is {computer_point} and {a}'s point is {a_point}\n")        # showing the points of both after each try

    elif _input == "s" and _random == "p":
        a_point += 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("human gets 1 point\n")
        print(f"computer point is {computer_point} and {a}'s point is {a_point}\n")

    elif _input == "p" and _random == "s":
        computer_point += 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("computer gets 1 point\n")
        print(f"computer point is {computer_point} and {a}'s point is {a_point}\n")

    elif _input == "p" and _random == "r":
        a_point += 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("human gets 1 point\n")
        print(f"computer point is {computer_point} and {a}'s point is {a_point}\n")

    elif _input == "r" and _random == "s":
        a_point += 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("human gets 1 point\n")
        print(f"computer point is {computer_point} and {a}'s point is {a_point}\n")

    elif _input == "r" and _random == "p":
        computer_point += 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("computer gets 1 point\n")
        print(f"computer point is {computer_point} and {a}'s point is {a_point}\n")

    else:
        print("Invalid Input\n")   

print(f"{a}: {a_point}\nComputer : {computer_point}\n")                # showing total points of both


if computer_point > a_point:
    print("\t\t\t\t\tComputer Wins\n")

elif computer_point < a_point:
    print(f"\t\t\t\t\t {a} Wins\n")

else:
    print("Tie")

print("Run again to play more")
