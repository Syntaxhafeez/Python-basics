# accept name and age from the user. check if the user is a valid voter or not

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if age > 18:
    print(name, "is a valid voter")

else:
    print(name, "is a invalid voter")