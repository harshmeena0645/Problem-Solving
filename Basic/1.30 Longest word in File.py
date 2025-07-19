with open("file.txt", "r") as f:
    words = f.read().split()
    print("Longest word:", max(words, key=len))