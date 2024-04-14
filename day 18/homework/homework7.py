#User input word and search letter.
word = input("Enter word here: ")
operator = input("Enter letter here: ")
x = word.find(operator)

#Your task is to print the index of the first letter in the word, and if it doesn't exist, simply -1.
print(x)