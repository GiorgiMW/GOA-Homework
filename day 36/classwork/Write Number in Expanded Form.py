def expanded_form(num):
    num = str(num)
    strin = ""
    for x, i in enumerate(num):
        if i != "0":
            strin = strin + " + {}{}".format(i, len(num[x+1:])* "0")
    return strin.strip(" +")