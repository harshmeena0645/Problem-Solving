with open("file.txt", "r") as f:
    print("Word count:", len(f.read().split()))