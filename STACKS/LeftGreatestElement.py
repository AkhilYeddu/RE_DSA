# Using Stacks
arr = [11,10,6,5,10,7,4,8]
ans = [-1] * len(arr)
stack = []
for i in range(len(arr)):
    while len(stack) > 0 and stack[-1] <= arr[i]:
        stack.pop()
    if len(stack) > 0:
        ans[i] = stack[-1]
    stack.append(arr[i])
print(ans)