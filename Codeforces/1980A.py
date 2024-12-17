x = int(input())
for _ in range(x):
    a , round = map(int,input().split())
    word  = input()
    l = []
    missing = 0 
    no_of_A = 0
    no_of_B = 0
    no_of_C = 0
    no_of_D = 0
    no_of_E = 0
    no_of_F = 0
    no_of_G = 0
    for i in range(len(word)):
        if word[i] == "A":
            no_of_A+=1
        if word[i] == "B":
            no_of_B+=1
        if word[i] == "C":
            no_of_C+=1
        if word[i] == "D":
            no_of_D+=1            
        if word[i] == "E":
            no_of_E+=1
        if word[i] == "F":
            no_of_F+=1
        if word[i] == "G":
            no_of_G+=1 
    l.append(no_of_A)
    l.append(no_of_B)
    l.append(no_of_C)
    l.append(no_of_D)
    l.append(no_of_E)
    l.append(no_of_F)
    l.append(no_of_G)
    for i in l:
        if i < round:
            missing+= round - i
    print(missing)        
     