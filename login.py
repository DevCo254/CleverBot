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
    if User1 in UserList:     #is User1 in the list? 
        if Pass1 == PassList[UserList.index(User1)]:
            print ("Log in Success /n enter 1 if you are new 2 if not")
            x = int(input())
            if x == '1':
                print("State your vision")
                else:
                    print("whats new")
    else:
        print("Invalid Username and password")