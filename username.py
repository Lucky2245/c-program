import os
#Check if the file username.txt exists.
if os.path.exists("username.txt"):
    #Read the username file
    username = open("username.txt", "r")
    #output the content of the username file
    print("Welcome Back " + username.read())
else:
    #Ask the user to create a username
    username = input("Create a username ")
    #Create the file username.txt
    write_file = open("username.txt", "w")
    write_file.write(username)
    write_file.close()
    read_file = open("username.txt", "r")
    print("Your username is " + read_file.read())
    read_file.close()
