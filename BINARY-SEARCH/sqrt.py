# finding square root of a number using binary search
n = int(input())
low = 1
high = n
ans = 0
while low <= high:
    mid = (low+high) // 2
    if mid * mid <= n:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)