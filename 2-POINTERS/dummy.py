arr = [1,0,1,1,0,1,0,0,1,1,1,0]
i = 0
j = 0
n = len(arr)
ans = 0
c = 0
k = 2

while j < n:
    if arr[j] == 1 or c < k:
        ans = max(ans,j-i+1)
        if arr[j] == 0:
            c+=1
        j+=1
    else:
        if arr[i] == 0:
            c-=1
        i+=1
    

print(ans)
