d = {}
arr = [2,6,3,2,8,7,2,3,8,7]
for i in range(len(arr)):
    if arr[i] not in d:
        d[arr[i]]=0
    d[arr[i]]+=1
print(d)              