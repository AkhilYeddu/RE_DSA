t = int(input())
for _ in range(t):
    n= int(input())
    x,y= map(int,input().split())
    if n==0:
        print(0)
        continue
    put= (n + y - 1)//y
    blend= (n + x - 1)//x
    print(max(put,blend))