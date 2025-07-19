dict = {"a": 1, "b": 2}
dict["c"] = 3
print(dict)


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print("Merged dictionary:", dict1)


dictionary = {"a": 1, "b": 2}
for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}")