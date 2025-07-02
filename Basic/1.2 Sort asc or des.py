arr = [50, 20, 40, 10, 30]

asc_sorted = sorted(arr)
desc_sorted = sorted(arr, reverse=True)

print("Original array:", arr)
print("Ascending order:", asc_sorted)
print("Descending order:", desc_sorted)



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

output ['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

output ['banana', 'cherry', 'Kiwi', 'Orange']



def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

output [50, 65, 23, 82, 100]
