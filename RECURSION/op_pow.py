def pow(x,y):
    if y == 0:
        return 1
    half = pow(x,y//2)
    if y % 2 == 0:
        return half * half
    else:
        return half * half * x
x,y = map(int,input().split())
n = pow(x,y)
print(n)