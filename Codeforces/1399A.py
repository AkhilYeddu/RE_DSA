x = int(input())
for _ in range(x):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    flag = False
    while True:
        if len(nums) == 1:
            flag = True
            break
        if nums[1] - nums[0] <= 1:
            nums.remove(min(nums[0],nums[1]))
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
        
        

        
