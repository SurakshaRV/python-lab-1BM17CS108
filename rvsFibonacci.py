def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))

n=int(input("how many numbers? "))
if n<=0:
    print("enter a positive integer: ")
else:
    for i in range(1,n+1):
        print(fib(i))
