
name = "python"
passkey = "123thon@"

username = input("enter your user name: ")
password = input("enter your password: ")
attempts = 0
if password == "123thon@" and username == "python": # if password is correct returns succesful
    print("login succesful")
while password != "123thon@" or username != "python": # if password not correct gives the user 3 try
    print("pls check your password or username and try again")
    username = input("enter your user name: ")
    password = input("enter your password: ")
    if password == "123thon@" and username == "python": # if password is correct returns succesful
        print("login succesful")

    attempts = attempts+1 # help count the num of tries it does not exceed 3 0r 4
    if attempts >=3: # if tries is >=3 tells user to try again
        print("too many attempts failed")
        print ("try agin later")
        break
    

