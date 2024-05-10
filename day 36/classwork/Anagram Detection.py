def is_anagram(test, original):
    x = test.lower()
    y = original.lower()
    c = sorted(x)
    d = sorted(y)
    if c == d:
        return True
    else:
        return False
        