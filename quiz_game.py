print("welcome to the quiz game")
user = input("do you want to play?  ")
if user == "yes":
    print("okay , let's start the game..")
else:
    quit()
    
score = 0

answer = input("What is CPU? ")
if answer == "central processing unit":
    print("it's correct")
    print("Well played ")
    score+=1
else:
    print("incorrect")

answer = input("What is GPU? ")
if answer == "graphics processing unit":
    print("it's correct")
    print("Awesome ")
    score+=1
else:
    print("incorrect")

answer = input("What is RAM? ")
if answer == "random access memory":
    print("it's correct")
    print("your playing well ")
    score+=1
else:
    print("incorrect")

answer = input("What is ROM? ")
if answer == "read only memory":
    print("it's correct")
    print("Your genius  ")
    score+=1
else:
    print("incorrect")

print(f"your total score is {score} for correct answers.")