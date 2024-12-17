x = int(input())
for i in range(x):
    y = int(input())
    arr = list(map(int,input().split()))
    even = []
    odd = []
    for i in range(len(arr)):
        if arr[i]%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    if(sum(even)>sum(odd)):
        print("YES")
    else:
        print("NO")    