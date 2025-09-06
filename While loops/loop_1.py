# separate each digit of a number and print it on the new line

num = int(input("Enter a number: "))
digits = []

while num > 0:
    digits.append(num % 10)
    num //= 10

for i in reversed(digits):
    print(i)