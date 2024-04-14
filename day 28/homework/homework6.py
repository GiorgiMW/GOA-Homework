def solution(s):
    result = ""
    for letter in s:
        if letter != letter.upper():
            result = result + letter
        elif letter == letter.upper():
            result = result + " " + letter
    return result
