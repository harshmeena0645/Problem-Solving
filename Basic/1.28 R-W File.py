with open("file.txt", "w") as f:
    f.write("Hello, this is a file!")
with open("file.txt", "r") as f:
    print(f.read())