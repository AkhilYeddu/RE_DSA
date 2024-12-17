a = [3,7,8,10,11,14]
b = [2,6,9,12,14,21]
p1 = 0
p2 = len(b) - 1
k = 25
ans = float('inf')
while p1 < len(a) and p2 >=0:
    s = a[p1] + b[p2]
    if abs(s-k) < ans:
        ans = abs(s-k)
    if s > k:
        p2-=1
    else:
        p1+=1
print(ans)