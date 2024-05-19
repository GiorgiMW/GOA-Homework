def is_pangram(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    is_true = True
    for i in letters:
        if i in s.lower():
            is_true = True
        else:
            is_true = False
            break
    return is_true