def rec(n):
    if x == 0:
        return 1
    
    rec(x-1)
    res+=x
    if res == n:
        return x
    
    
x = int(input())
n = rec(x)
print(n)