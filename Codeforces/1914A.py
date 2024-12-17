x = int(input())
for _ in range(x):
    n = int(input())
    log = input()
    my_set = set()
    time = {}
    for i in range(len(log)):
        if log[i] not in time:
            time[log[i]] = 1
        else:
            time[log[i]] += 1
        if time[log[i]] >= ord(log[i]) - ord('A') + 1:
            my_set.add(log[i])
    print(len(my_set))