#Create the copy of join function
def copy_join(listn):
    text_string = ""
    for i in listn:
        text_string = text_string + i + " "
    return text_string

my_list = ["Banana", "audi", "frog", "gold", "shovel"]
print(copy_join(my_list))