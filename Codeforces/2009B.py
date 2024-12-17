x = int(input())
for i in range(x):
    y = int(input())
    ans = []
    for i in range(y):
        col = input()
        for j in range(4):
            if col[j] == "#":
                ans.append(j+1)
    for i in range(len(ans)-1,-1,-1):
        if i == 0:
            print(ans[i])
        else:
            print(ans[i],end=" ")    