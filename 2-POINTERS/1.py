a = [3,7,8,10,11,14]
b = [2,6,9,12,14,21]
p1 = 0
p2 = len(a) - 1
k = 20
ans = float('inf')
while p1 < p2:
    s = a[p1] + b[p2]
    if abs(s - k) < ans:
        ans = abs(s-k)
    p1+=1
    p2-=1
print(ans)