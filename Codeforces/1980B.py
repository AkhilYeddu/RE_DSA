x = int(input())
for _ in range(x):
    n,f,k = map(int,input().split())
    # n = no of test cases
    # f = index of the favourite cube
    # k = first k cubes to be removed

    cubes = list(map(int,input().split()))
    fav_cube = cubes[f-1]

    cubes.sort(reverse=True)
    flag1 = False
    flag2 = False
    for i in range(n):
        if i < k:
            if cubes[i] == fav_cube:
                flag1=True
        else:
            if cubes[i] == fav_cube:
                flag2=True
    if flag1 and flag2:
        print("MAYBE")
    elif flag1 and not flag2:
        print("YES")
    elif flag2 and not flag1:
        print("NO")