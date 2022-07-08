def sum():
    n=int(input("Please Enter your number:"))
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
print(sum())