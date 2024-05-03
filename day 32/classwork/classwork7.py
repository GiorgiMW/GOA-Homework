def to_weird_case(words):
    str = words.split()
    sentence = []
    for i in str:
        str2 = ""
        for x in range(len(i)):
            if x % 2:
                str2 = str2 + i[x].lower()
            else:
                str2 = str2 + i[x].upper()
        sentence.append(str2)
    return " ".join(sentence)