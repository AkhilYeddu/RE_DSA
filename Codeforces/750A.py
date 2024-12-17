n,k = map(int,input().split())
new_year = 1440
start = 1200
start = start + k
time_remaining = new_year - start
ans = 0
time = 0
for i in range(1,n+1):
    time += 5*i
    if time <= time_remaining:
        ans+=1
    else:
        break
print(ans)