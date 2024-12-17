x = int(input())
l = list(map(int,input().split()))
for i in range(len(l)):
    l[i] = abs(l[i])
print(min(l))    