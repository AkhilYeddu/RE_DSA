def fact(x):
    if x == 1:
        return 1
    return fact(x-1)*x
x = int(input())
n = fact(x)
print(n)
