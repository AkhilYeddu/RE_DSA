x = int(input())
for _ in range(x):
    n = int(input())
    s = input()
    bin = []
    count = 0
    for i in range(1,n):
        word = s[i-1]+s[i]
        if word not in bin:
            bin.append(word)
            count+=1
    print(count)
