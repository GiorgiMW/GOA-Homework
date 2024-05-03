def capitals(word):
    answer = []
    for i in range(len(word)):
        if word[i].isupper():
            answer.append(i)
    return answer