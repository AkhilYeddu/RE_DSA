s = list(input())
n = len(s)
possible = True

for i in range(n//2):
    left = s[i]
    right = s[n-i-1]
    if left == "?" and right == "?":
        s[i]=s[n-i-1]="a"
    elif left == "?":
        s[i]=right
    elif right=="?":
        s[n - i - 1]=left
    elif left!=right:
        possible=False
        break
if n%2==1 and s[n//2] == "?":
    s[n//2] = "a"
if possible:
    print("".join(s))
else:
    print("-1")
