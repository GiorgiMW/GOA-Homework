#Enter the user's first name, then last name. Save them in a list and, like the previous task, work on all elements with the capitalize method
name = input("Enter you name here: ")
lastname = input("Enter your lastname here: ")
listn = [name, lastname]
x = listn[0][0].upper()
y = listn[1][0].upper()

#Your task is to output the user's initials as a string. test case: input) "Data", "Tezelashvili" -> output: "D.T"
print(x + "." + y)