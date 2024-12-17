x = int(input())
for _ in range(x):
    length = int(input())
    password = input()
    nums = []
    letters = []
    for i in range(len(password)):
        if "a"<=password[i]<="z":
            letters.append(password[i])
        else:
            nums.append(password[i])

    valid =""
    for i in sorted(nums):
        valid+=i
    for i in sorted(letters):
        valid+=i
    if valid == password:
        print("YES")
    else:
        print("NO")    
    
        