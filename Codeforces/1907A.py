n = int(input())
for _ in range(n):
    move = input()
    letter = move[0]
    number = int(move[1])
    moves = []
    r = ["a","b","c","d","e","f","g","h"]
    for i in range(1,9):
        if i == number:
            pass
        else:
            moves.append(letter+str(i))
    for i in r:
        if i == letter:
            pass
        else:
            moves.append(i+str(number))
    for i in moves:
        print(i)