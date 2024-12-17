def rec(x):
    if x == 0:
        return
    rec(x-1)
    n = x
    while n > 0:
        print(x,end=" ")
        n-=1
x = int(input())
rec(x)