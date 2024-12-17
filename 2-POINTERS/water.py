
arr = [3,7,4,7,3,6,4,1,2]
n = len(arr)
p1 = 0
p2 = n - 1
ans = -1

while p1 < p2:
    area = min(arr[p2],arr[p1]) * (p2 - p1)
    ans = max(ans,area)
    if arr[p1] < arr[p2]:
        p1 += 1
    else:
        p2 -= 1
print(ans)



