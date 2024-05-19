def duplicate_encode(word):
    word = word.lower()
    answer = ""
    for i in word:
        if word.count(i) > 1:
            answer = answer + ")"
        if word.count(i) == 1:
            answer = answer + "("
    return answer