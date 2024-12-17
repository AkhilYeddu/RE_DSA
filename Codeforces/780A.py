x = int(input())
l = list(map(int,input().split()))
table = set()
ans = 0
for i in l:
    if i in table:
        table.remove(i)
    else:
        table.add(i)
    ans = max(len(table),ans)
print(ans)