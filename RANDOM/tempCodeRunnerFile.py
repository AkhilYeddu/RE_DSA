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