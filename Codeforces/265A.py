s = input()
t = input()
p = 0
for i in t:
    if p < len(s) and s[p] == i:
        p+=1
print(p+1)
