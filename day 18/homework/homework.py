name = input("Enter your name here: ")

def test_lower(words):
    if name == name.lower():
        return f"Your name is in lowercase {name}"
    else:
        return f"Your name isn't lowercase {name}"
    
print(test_lower(name))