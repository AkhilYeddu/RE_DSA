    a,b = map(int,input().split())
    m = min(a,b)
    while True:
        if m % a == m % b:
            break
        m += 1
    print(m)