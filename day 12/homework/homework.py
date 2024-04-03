#Enter the user's first name, last name, age and place of residence. Add each of them to the list using append. Using slicing,
name = input("Enter your name here: ")
lastname = input("Enter your lastname here: ")
age = input("Enter your age here: ")
user_location = input("enter where you live here: ")
list = []

list.append(name)
list.append(lastname)
list.append(age)
list.append(user_location)

#print 1: First Name, Last Name,
print("1: ", list[0:2])

#2: Last Name, Age,
print("2: ", list[1:3])

#3: First Name, Last Name.
print("3: ", list[0:4])

#Age 4: Last Name, Age, Residence.
print("4: ", list[1:4])