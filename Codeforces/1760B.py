x = int(input())
for i in range(x):
    y = int(input())
    word = input()
    word = sorted(word)
    least = word[len(word)-1]
    print(ord(least)-ord('a') + 1)