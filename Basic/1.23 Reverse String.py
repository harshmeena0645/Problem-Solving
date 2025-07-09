name=str("HarshMeena")
ans=name[::-1]
print(ans)



def reverse_string(s):
    return ''.join(reversed(s))
print(reverse_string("hello"))
# Output: "olleh"



def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("hello"))
# Output: "olleh"