def pow(x,y):
    if y == 0:
        return 1
    return pow(x,y-1)*x 
x,y = map(int,input().split())
print(pow(x,y))

