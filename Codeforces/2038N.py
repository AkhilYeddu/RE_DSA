n = int(input())
for _ in range(n):
    statement = input()
    num1 = statement[0]
    symbol = statement[1]
    num2 = statement[2]
    if symbol == "=":
        if int(num1) == int(num2):
            print(statement)
        elif int(num1) > int(num2):
            print(str(num1)+">"+str(num2))
        else:
            print(str(num1)+"<"+str(num2))
    if symbol == ">":
        if int(num1) == int(num2):
            print(str(num1)+"="+str(num2))
        elif int(num1) > int(num2):
            print(statement)
        else:
            print(str(num1)+"<"+str(num2))
    if symbol == "<":
        if int(num1) == int(num2):
            print(str(num1)+"="+str(num2))
        elif int(num1) > int(num2):
            print(str(num1)+">"+str(num2))
        else:
            print(statement)