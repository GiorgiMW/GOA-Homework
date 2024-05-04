def kebabize(st):
    answer = ""
    for i in st:
        if i.isalpha() == False:
            i = ""
        if i.isupper():
            i = i.lower()
            answer = answer + "-" + i
        else:
            answer = answer + i
    return answer.strip("-")