x = int(input())
for _ in range(x):
    n, m = map(int, input().split())
    size = 0
    count = 0
    words = []
    for _ in range(n):
        word = input().strip()
        words.append(len(word))
    for i in range(len(words)):
        if size + words[i] <= m:
            size += words[i]
            count+=1
        else:
            break

    print(count)
        
