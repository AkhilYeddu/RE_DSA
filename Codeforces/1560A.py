x = int(input())
for _ in range(x):
    n = int(input())
    i = 1
    l = [1,2]
    for i in range(3,2*n+1):
        s_i = str(i)
        decimal_check = len(s_i) - 1 
        if i % 3 == 0 or s_i[decimal_check] == "3":
            pass
        else:
            l.append(i)       
    print(l[n-1])