arr = [12,12,6,6,21,21,7,7,9,9,4,4,10,10]
l = 0
h = len(arr) - 1
if len(arr) % 2 == 0:
    print("NO")
else:
    while l <= h:
        mid = (l+h) // 2
        if arr[mid] == arr[mid-1]:
            mid = mid - 1
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            break
        elif mid % 2 == 0:
            l = mid + 2
        else:
            h = mid - 1
    print(arr[mid])
    
   

    

