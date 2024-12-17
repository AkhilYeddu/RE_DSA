def pow(x,y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return pow(x,y//2) + pow(x,y//2)
    else:
        return pow(x,y//2)+pow(x,y//2)*x
x,y = map(int,input().split())
n = pow(x,y)
print(n)