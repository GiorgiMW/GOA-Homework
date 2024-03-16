degrees = int(input("enter your country temperature(in °C): "))

if degrees < 20:
    print("Cold")
elif degrees > 20 and degrees <= 30:
    print("Warm")
elif degrees > 30:
    print("Hot")