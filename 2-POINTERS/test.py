arr = [1,3,1,5,4]
d = {}
k = 0
count = 0
for i in range(len(arr)):
    if arr[i] not in d:
        d[arr[i]] = 1
    else:
        d[arr[i]] += 1
for key in d:
    if k == 0:
        if d[key] > 1:
            count += 1
    elif key + k in d:
        count += 1
print(count)
