arr = ["a","b","c","a","b","c","d","d"]
i = 0
j = 0
my_set = set()
n = len(arr)
ans = 0
while j < n:
    if arr[j] not in my_set:
        my_set.add(arr[j])
        j+=1
        ans = max(ans,len(my_set))
        
    else:
        my_set.remove(arr[i])
        i+=1
print(ans)
