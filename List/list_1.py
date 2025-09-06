# print positive and negative elements of an list

numbers = [12, -7, 5, -3, 9, -1, 2]

positive = []
negative = []

for num in numbers:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive", positive)
print("Negative", negative)