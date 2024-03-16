age = int(input("Enter your age here: "))

if age >= 0 and age < 13:
    print("you are a kid")
elif age >= 13 and age < 18:
    print("You are the teenager")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("Your are old")


movie_list = ["home alone", "Thor", "never back down"]
print(movie_list)
print(movie_list[0])