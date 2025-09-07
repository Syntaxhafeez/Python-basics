# write a python program to combine two dictionary by adding values for common keys

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 25}

combined = {}

for key in set(dict1) | set(dict2):
    combined[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(combined)
