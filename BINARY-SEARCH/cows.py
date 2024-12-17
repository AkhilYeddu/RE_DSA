def check(n,cows,arr,mid):
    p = arr[0]
    c = 1
    for i in range(1,n):
        if arr[i] - p >= mid:
            p = arr[i]
            c+=1
        if c == cows:
            return True
    return False

arr = [0,3,4,7,9,10]
n = len(arr)
cows = 4
low = float('inf')
for i in range(1,len(arr)):
    if arr[i] - arr[i-1] < low:
        low = arr[i] - arr[i-1]
high = arr[len(arr)-1] - arr[0]
ans = low
while low <= high:
    mid = ( low + high ) // 2
    if check(n,cows,arr,mid):
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)