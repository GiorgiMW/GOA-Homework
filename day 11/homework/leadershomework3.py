#Password Verification: Write a program that prompts the user for a password.
while True:
    password = input("Enter a password here: ")
    
    if password != "12345678":
        print("that's not correct try again.")
    elif password == "12345678":
            break
print("access granted")

#Continue reading until the correct password is entered. Assume the correct password is "12345678".
