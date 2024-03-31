def copy_replace(name,name2,name3):
    listn = ["name","name2","name3"]
    print("first words: ", listn)
    return(name,name2,name3)

word = "Car"
word1 = "house"
word2 = "pc"
new_word = copy_replace(word,word1,word2)
print("replaced words:", new_word)