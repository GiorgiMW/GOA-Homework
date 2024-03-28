#Create a function that passes a string. Your task is to remove all spaces from this string 
def info(word):
    words = word.split()
    y = "".join(words)
    print(y)

#and print it like this test case: input) "Goal-Oriented Academy" -> output) "Goal-OrientedAcademy"
word = "     Goal-   Oriented   Academy    "
info(word)
    