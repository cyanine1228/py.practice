def mex(a):
    i = 0
    while i in a:
        i += 1
    return i

board = [[0] * 60 for i in range(25)]
for i in range(25):
    for j in range(60):
        a = set()
        for p in range(i):
            a.add(board[p][j])
        for q in range(j):
            a.add(board[i][q])
        k = 1
        while (i - k >= 0) & (j - k >= 0):
            a.add(board[i - k][j - k])
            k += 1
        board[i][j] = mex(a)
# board = [[king(i, j) for i in range(24)]for j in range(24)]
for i in range(25):
    for j in range(60):
        print("{0:2d}".format(board[i][j]), end = " ")
    print("")