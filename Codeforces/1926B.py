x = int(input())
for _ in range(x):
    n = int(input())
    pattern = []
    for i in range(n):
        line = input()
        count = 0
        for each in line:    
            if each == "1":
                count += 1
        pattern.append(count)
    ans = []            
    for j in range(len(pattern)):

        if pattern[j] != 0:
            ans.append(pattern[j])
    ans = sorted(ans)
    if ans[0] == ans[1]:
        print("SQUARE")
    else:
        print("TRIANGLE")        