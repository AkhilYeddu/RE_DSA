x = int(input())
for _ in range(x):
    n = int(input())
    s = input()
    i = 0
    d = 0
    while i < n-2:
        if s[i:i+3] == "pie" or s[i:i+3] == "map":
            d+=1
            i+=3
        else:
            i+=1
    print(d)