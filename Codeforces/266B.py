x,y=map(int,input().split())
queue = list(input())
for _ in range(y):
    i=0
    while i < x-1:
        if queue[i] == "B" and queue[i+1] == "G":
            temp = queue[i]
            queue[i] = queue[i+1]
            queue[i+1] = temp
            i+=1
        i+=1               
print("".join(queue))           
