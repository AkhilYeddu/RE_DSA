arr = [4,-3,-1,2,-2]
psum = [0] * len(arr)
psum[0] = arr[0]
for i in range(1,len(arr)):
    psum[i] = psum[i-1] + arr[i]
print(psum)

# psum_set = set(psum)
# print(psum_set)
# if len(psum) != len(psum_set) or 0 in psum_set:
#     print("Yes")
# else:
#     print("No")