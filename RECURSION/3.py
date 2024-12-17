def rec(x):
    if x == 0:
        return 0
    return rec(x//10) + x % 10
x = int(input())
n = rec(x)
print(n)
