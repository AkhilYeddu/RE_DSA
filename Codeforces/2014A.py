x = int(input())
for _ in range(x):
    robin = 0
    count = 0
    a,b =  map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        if arr[i] >= b:
            robin +=arr[i]
        elif arr[i] == 0 and robin > 0:
            robin -=1
            count +=1
        else:
            pass    
    print(count)               

