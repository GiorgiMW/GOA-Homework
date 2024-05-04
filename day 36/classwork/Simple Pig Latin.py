def pig_it(text):
    text = text.split()
    lstn = []
    for i in text:
        string = ""
        if i.isalpha():
            string += i[1:] + i[0] + "ay"
        else:
            string = string + i
        lstn.append(string)
    return " ".join(lstn)
            