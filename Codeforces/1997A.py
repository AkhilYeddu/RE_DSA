x = int(input())
f = False
for i in range(x):
    username,before,after = map(str,input().split())
    before = int(before)
    after = int(after)
    f = True if before >= 2400 and after > before else False
    if f:
        print("YES")
        break
if not f:
    print("NO")
       
    