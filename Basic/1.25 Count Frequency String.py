string = input("Enter a string: ")
frequency = {char: string.count(char) for char in set(string)}
print("Frequency:", frequency)