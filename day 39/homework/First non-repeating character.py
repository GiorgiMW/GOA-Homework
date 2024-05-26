def first_non_repeating_letter(s):
    string = ""
    for i in s:
        if s.lower().count(i.lower()) == 1:
            string = string + i
    if string == "":
        return string
    else:
        return string[0]