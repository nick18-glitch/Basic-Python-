import random

#loop 
count = 0
while True:
    choice = input("Roll your dice? (y/n):").lower()
#if user == y print two random number
    if choice == "y" :
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        count +=1
        print(f"({d1,d2})")
        
#if n the end the game and also print a thankyou message
    elif choice == "n":
        print("Thankyou")
        print(f"you haves rolled {count} times ")
        break
#else any other input = invalid input
    else:
        print("Invalid input.")