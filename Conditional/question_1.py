# Question: Accept two numbers and print the greatest between them

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

if num1 > num2:
    print(num1, "Is the greatest number")

elif num2 > num1:
    print(num2, "Is the greatest number")

else:
    print("both numbers are equal")