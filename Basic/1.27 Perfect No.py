num=28
sum=sum(i for i in range(1, num) if num % i == 0)
if sum == num:
    print("Perfect")
else:
    print("Not Perfect")