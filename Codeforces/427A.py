n = int(input())
order = list(map(int,input().split()))
polices = 0
untreated = 0
for event in order:
    if event == -1:
        if polices > 0:
            polices -= 1
        else:
            untreated += 1
    else:
        polices += event
print(untreated)                    





