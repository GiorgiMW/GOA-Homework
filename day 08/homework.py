#Create two variables name - password where you enter the customer's name and password and also create a third variable repeat_password where if the password entered by the user does not match the password entered for the first time write that the password is incorrect or write "You have successfully registered" - use if - else
name = input("Please enter your name here: ")
password = input("Please enter your password here: ")
repeat_password = input("Please enter your password here: ")

if password != repeat_password:
    print("Wrong password")
else:
    print("Password confirmed")