x = int(input())
for _ in range(x):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    i,j,k,l = arr[n-1],arr[0],arr[n-2],arr[1]
    print(abs(i-j)+abs(j-k)+abs(k-l)+abs(l-i))