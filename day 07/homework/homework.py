#Output the even numbers from one to one using a loop and a range
for i in range(0,10,2):  #range(start,end,step.)
    print(i)

#Output the numbers from one to twenty through the while loop
num1 = 1
while num1 <= 20:
    print(num1)
    num1 = num1 + 1

#Add the numbers from zero to five through the while loop
counter = 1
summation = 0
while counter <= 5:
    print(counter)
    summation = summation + counter
    counter = counter + 1
print(summation)

#Use any string in the for loop and test how it works, output one character of the string at each iteration
for i in range(15):
    print("Hello world")

for i in "Hello world":
    print(i)