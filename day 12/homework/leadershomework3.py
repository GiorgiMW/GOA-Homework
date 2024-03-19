#Create a registration algorithm. Ask the user for their first name, last name, age and email.
user_name = input("Enter your name here: ")
user_lastname = input("Enter your lastname here: ")
user_age = input("Type your age here: ")
user_email = input("Type your email here: ")

#and finally present the received information in one sentence.
print(f"Hello {user_name} {user_lastname}, you are {user_age} years old and your email is: {user_email}" )