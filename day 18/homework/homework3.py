#Enter a word for the user. Your task is to convert letters at even indices to uppercase and those at odd indices to lowercase,
name = input("Enter random word here: ")
listn = []
listn2 = []
for i in name:
    listn.append(i)
    if listn.index(i) % 2 == 0:
        listn2.append(i.upper())
    else:
        listn2.append(i.lower())
if len(listn2) % 2 == 0:
    listn2[-1] = listn2[-1].lower()
else:
    pass

#and finally print the result.
print("".join(listn2))