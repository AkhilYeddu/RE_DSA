n,m = map(int,input().split())
base = n // m
extra = n % m
candies = []
for i in range(m - extra):
    candies.append(base)
for i in range(extra):
    candies.append(base+1)
for i in range(len(candies)):
    if i == len(candies)-1:
        print(candies[i])
    else:
        print(candies[i],end=" ")            

