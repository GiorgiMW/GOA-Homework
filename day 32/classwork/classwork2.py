def open_or_senior(data):
    categor = []
    for i in data:
        if i [0] >= 55 and i[1] > 7:
            categor.append("Senior")
        else:
            categor.append("Open")
    return categor