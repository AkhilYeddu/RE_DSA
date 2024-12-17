import sys
n = int(input())
summ = list(map(int,input().split()))
t_sum = 0
t_sum = sum(summ)
minn = float('inf')
if t_sum % 2 == 0:
    print(t_sum)
else:
    for i in summ:
        if i % 2 != 0:

            minn = min(i,minn)
    print(t_sum-minn)
