# this class was all about PREFIXSUM ARRAY.
sum = [1,2,3,4,5]
psum = [0] * len(sum)
s = 0
for i in range(len(sum)):
    s = s + sum[i]
    psum[i] = s 
print(psum)