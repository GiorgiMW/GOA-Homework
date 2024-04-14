#Vowel Count
def get_count(sentence):
    num = 0
    for i in ["a", "e", "i", "o", "u"]:
        num = num + sentence.count(i)
    return num