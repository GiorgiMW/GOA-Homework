#Create a function that passes the four sides of a rectangle to calculate its perimeter.
width = int(input("Type width here: "))
height = int(input("Type height here: "))

def rectangle(width,height):
    print((width + height) * 2)

rectangle(width,height)