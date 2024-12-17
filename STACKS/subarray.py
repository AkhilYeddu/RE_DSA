arr = [2,3,13,7,6,9,5,3,2,11,2]
n = len(arr)
ans = 0
for i in range(n):
    for j in range(i,n):
        ans += max(arr[i:j+1])
print(ans)
