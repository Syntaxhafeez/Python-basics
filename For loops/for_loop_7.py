# count all letters, digits, and special symbols from a given string: str1 = P@#yn26at^&i5ve

str1 = "P@#yn26at^&i5ve"

Chars = 0
Digits = 0
Symbol = 0

for ch in str1:
    if ch.isalpha():
        Chars += 1
    elif ch.isdigit():
        Digits += 1
    else:
        Symbol += 1

print("Chars = ", Chars)
print("Digits = ", Digits)
print("Symbol = ", Symbol)