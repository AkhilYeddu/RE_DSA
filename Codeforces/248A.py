x = int(input())
left = []
right = []

for _ in range(x):
    a,b = map(int,input().split())
    left.append(a)
    right.append(b)
on_left = 0
off_left = 0
on_right = 0
off_right = 0
for i in left:
    if i == 1:
        on_left+=1
    else:
        off_left+=1
for i in right:
    if i == 1:
        on_right +=1
    else:
        off_right +=1
print(min(on_left,off_left)+min(on_right,off_right))
                        
