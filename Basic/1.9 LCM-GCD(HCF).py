a=12
b=15
x=a
y=b
while b:
    a,b=b,a%b

HCF=a
print("HCF:", HCF)

LCM = x * y // HCF
print("LCM:", LCM)


GCD of array

Sample Input 0
5
2 4 6 8 16
Sample Output 0
2

Sample Input 1
3
1 2 3
Sample Output 1
1

--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x
# GCD of Array

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def func(l):
    res = l[0]
    for i in range(1, len(l)):
        res = gcd(res, l[i])
    return res
n = int(input())
l = list(map(int, input().split()))
print(func(l))
