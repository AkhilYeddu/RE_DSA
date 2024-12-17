row1 = input()
row2 = input()
row3 = input()
vertical_flag =True
if row1[0] == row3[2] and row1[1] == row3[1] and row1[2] == row3[0] and row2[0] == row2[2]:
    print("YES")
else: 
    print("NO")   
