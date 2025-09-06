# if elif ladder: take the input of temerature in celcius

temp = float(input("Enter Temperature: "))

if temp <= 0:
    print("Freezing cold")
elif temp >= 0 and temp <= 10:
    print("Very cold")
elif temp >= 10 and temp <= 20:
    print("Cold")
elif temp >= 20 and temp <= 30:
    print("Pleasant")
elif temp >= 30 and temp <= 40:
    print("Hot")
elif temp >= 40:
    print("Very Hot")

else:
    print("Invalid temperature!")