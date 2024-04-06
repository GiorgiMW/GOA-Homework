#Your task is to create the same logic as you did in the previous task, just without the find method - use a loop.
word = input("Enter word here: ")
operator = input("Enter letter here: ")
listn = []
for i in word:
    listn.append(i)
if operator in listn:
    print(word.index(operator))
    
#Finally test the performance of both algorithms and check if you get the same results.
else:
    print(-1)