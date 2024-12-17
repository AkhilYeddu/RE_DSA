x = int(input())
for _ in range(x):
    y = int(input())
    arr = list(map(int,input().split()))
    flag = False
    while not flag:
        flag = True
        for i in range(1,y-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = False
    if arr == sorted(arr):
        print("YES")
    else:
        print("NO")    
        
