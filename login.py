UserList = []
PassList = []

print("welcome to Devco")

ans = input("Do you have an account with Devco y/n:")

if ans =='n':
    User = input("Please enter your username : ")
    UserList.append(User)
    Pass = input("please enter your password : ")
    PassList.append(Pass)
    print(UserList,Pass)
    print("account succesfuly registered Please Login")
    User1 = input("please enter your username : ")
    Pass1 = input("enter your password : ")
    if User1 == (UserList) and Pass1 == (PassList):
        print("Welcome to Devco")

    else:
            print("Invalid Username and password")