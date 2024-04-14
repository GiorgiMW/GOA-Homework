#Store your name in the variable.
name = input("Enter your name here: ")
def upper_lower(word):
    if len(name) > 5:
        return name.upper()
    else:
        return name.lower()
    
#If it's longer than five, convert the whole word to uppercase, otherwise to lowercase. Finally, print the converted name.
print(upper_lower(name))