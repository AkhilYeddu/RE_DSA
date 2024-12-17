arr = [6,10,10,6,14,14,10]
d = {}
k = 4
count = 0
for i in range(len(arr)):
    if arr[i]-k in d:
        count += d[arr[i]-k]

    if arr[i] not in d:
        d[arr[i]] = 0
    d[arr[i]]+=1
print(d)
print(count)