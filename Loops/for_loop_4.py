# take a number as input and print its table

n = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")