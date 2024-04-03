#Create a function that has a given word and checks if it is a palindrome
words = input("Enter word here: ")

def palin(words):
    if words == words[::-1]:
        print("Your word is palindrome")
    else:
        print("Your word isn't palindrome")

#(a word is a palindrome if its inverse also results in people, e.g. level)
palin(words)