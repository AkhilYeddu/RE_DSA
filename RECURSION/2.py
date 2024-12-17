def inc(x):
    if x == 0:
        return
    print(x,end=" ")
    inc(x-1)
    print(x,end=" ")
x = int(input())
inc(x)
