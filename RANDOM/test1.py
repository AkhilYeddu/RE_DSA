arr = [2,4,9,3,8,3,5,8,9,8,9]
k = 5
d = {}
for i in range(k):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1
print(len(d),end = " ")
s = 1
e = k
while e < len(arr):
    d[arr[s-1]] -= 1 
    if d[arr[s-1]] == 0 :
        del d[arr[s-1]]
    if arr[e] in d:
        d[arr[e]] +=1
    else:
        d[arr[e]] = 1
    print(len(d),end = " ")
    s+=1
    e+=1
    
 