# LOCAL MAXIMA

# BRUTE FORCE ->
# arr = [1,2,3,4,5,7,8,9]
arr = [1,2,8,3,1,6,5]
# local_maxima = []
# n = len(arr)
# if arr[0] > arr[1]:
#     local_maxima.append(arr[0])
# if arr[n-1] > arr[n-2]:
#     local_maxima.append(arr[n-1])
# for i in range(1,n-1):
#     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#         local_maxima.append(arr[i])
# print(local_maxima)

l = 0
h = len(arr)-1
while l <= h:
    mid = (l+h) // 2
    if(mid==len(arr)-1):
        break
    if(mid==0):
        break
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        break
    elif arr[mid] < arr[mid+1]:
        l = mid + 1
    else:
        h = mid - 1
print(arr[mid])
    