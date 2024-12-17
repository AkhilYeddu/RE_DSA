import math
x = int(input())
for _ in range(x):
    n = int(input())
    l = list(map(int,input().split()))
    a = sum(l)
    if int(math.sqrt(a)) == math.sqrt(a):
        print("YES")
    else:
        print("NO")