import random

start = input("Do you want to play? (yes/no): ").lower()
if start != "yes":
    quit()

user_wins = 0
comp_wins = 0
game_count = 0
while True:
    user = input("Enter your choice: ").lower()
    obj = ("rock","paper","scissors")
    comp = random.choice(obj)
    

    if user == comp:
        print(f"computer chose {comp} , it's a draw")

    elif user == "rock" and comp == "paper":
        print(f"computer chose {comp} ,you win! ")
        user_wins += 1
        game_count += 1

    elif user == "rock" and comp == "scissors":
        print(f"computer chose {comp} ,you lose!" )
        comp_wins += 1
        game_count += 1

    elif user == "paper" and comp == "rock":
        print(f"computer chose {comp} ,you win!" )
        user_wins += 1
        game_count += 1

    elif user == "paper" and comp == "scissors":
        print(f"computer chose {comp} ,you lose!" ) 
        comp_wins += 1  
        game_count += 1

    elif user == "scissors" and comp == "rock":
        print(f"computer chose {comp} ,you lose!" )
        comp_wins += 1
        game_count += 1

    elif user == "scissors" and comp == "paper":
        print(f"computer chose {comp} ,you win!" )
        user_wins += 1
        game_count += 1 
    elif user == "stop":
        print("thanyou for playing!")
        print(f"In the game you win {user_wins} times and computer win {comp_wins} times")
        print(f"The total game played by the user is {game_count} times")
        break
    else:
        print("invalid input.")

