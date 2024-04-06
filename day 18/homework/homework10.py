#Have the user input five words and add them all to one list. Then ask for the value to be joined, e.g. "-" / "+" / "^" etc. Your task is to work on the list: append only the even-indexed words with this concatenated value, and then add them to the common string. 
listn = []
for i in range(5):
    name = input("Enter your word here: ")
    listn.append(name)
operator = input("Enter operator here: ")
def oper(word):
    if operator == "+":
        word = "+".join(listn)
        return word
    elif operator == "-":
        word = "-".join(listn)
        return word
    else:
        return "Wrong operator"
    
    #Finally you need to print this string. Test case: input) ("python", "html", "css", "js", "git"), "+" -> output) "python+css+git".
print(oper(listn))
