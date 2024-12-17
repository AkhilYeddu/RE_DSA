s = input()
no_of_A = 0
otherwise = 0
for i in s:
    if i == "a":
        no_of_A +=1
    else:
        otherwise+=1 
if no_of_A > otherwise:
    print(len(s))
else:               
    print(len(s) - (otherwise-no_of_A+1))
