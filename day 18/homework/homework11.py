word = input("Enter a sentence to make all letters lowercase letters: ")
print(word.lower())

#Upper
word2 = input("Enter a sentence to make all letters uppercase letters: ")
print(word2.upper())

#Capitalize
word3 = input("Enter a sentence, essay or something to make first letters of sentence be uppercase letters: ")
print(word3.capitalize())

#Find
word4 = input("Enter a sentence: ")
findword = input("Enter a letter or word to find which index is it: ")
print(word4.find(findword))

#Join
listn = []
for i in range(5):
    string = input("Enter word here: ")
    listn.append(string)
print("-".join(listn))