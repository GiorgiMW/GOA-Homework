#Enter a word for the user. Using a for loop, check each of its letters and if any of them are lowercase, then input the word to the user from the beginning.
counter = 0
while True:
    word = input("Please enter a word: ")
    counter = counter + 1
    for i in word:
        if i.islower():
            print("Please enter the word again without lowercase.")
            break
    else:
        break

#Also print how many times the user had to enter the word - counter.
print("You entered the word without any lowercase letters after", counter, "attempt.")