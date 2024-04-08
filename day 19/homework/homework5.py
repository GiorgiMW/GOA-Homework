#Abbreviate a Two Word Name
def abbrev_name(name):
    string = name.split()
    letter1 = string[0][0]
    letter2 = string[1][0]
    
    return letter1.upper() + "." + letter2.upper()