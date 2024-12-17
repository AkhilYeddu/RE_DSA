n,d = map(int,input().split())
nums = list(map(int,input().split()))
count = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if abs(nums[i]-nums[j]) <= d and i!= j:
            count+=1
print(count)            