word1 = "abcd"
word2 = "pq"
ans = ""
min_length = min(len(word1),len(word2))
for i in range(min_length):
    ans+=word1[i]
    ans+=word2[i]
max_length = max(len(word1),len(word2))
if max_length == len(word1):
    for j in range(min_length,max_length):
        ans+=word1[j]
if max_length == len(word2):
    for j in range(min_length,max_length):
        ans+=word2[j]

print(ans)
