import math
cups = list(map(int,input().split()))
medals = list(map(int,input().split()))
sumof_cups = sum(cups)
sumof_medals = sum(medals)
shelves = int(input())
required = math.ceil(sumof_cups/5) + math.ceil(sumof_medals/10)
if shelves >= required:
    print("YES")
else:
    print("NO")    

    