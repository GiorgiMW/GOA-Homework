#Create a function that combines the functions we learned today (lower(), upper(), capitalize(), find())
def func(name):
    return (name.lower(), name.upper(), name.capitalize(), name.find("G"))

name1 = "Goa is the best"
    
print(func(name1))