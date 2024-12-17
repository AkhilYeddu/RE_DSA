n,k = map(int,input().split())
nums = list(map(int,input().split()))
count = 0
for i in range(len(nums)):
    if nums[i] + k <= 5:
        count+=1
if count >= 3:
    print(count//3)
else:
    print("0")