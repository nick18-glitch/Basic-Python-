master_password = input("what is your master password? ").lower()

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():
    account = input("account name: ")
    acc_password = input("password: ")

    with open('password.txt', 'a') as f:
        f.write(account + "|" + acc_password + "\n")
       

while True:
    mode = input("what you want to do add a new file or view existing one (view , add) ,press q to quit: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode ")
        continue
    
 