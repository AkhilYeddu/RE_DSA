def gcd(a,b):
    while b:
        a , b = b , a % b
    return a
x = int(input())
for _ in range(x):
    a,b = map(int,input().split())
    m = (a*b) // gcd(a,b)
    print(m)