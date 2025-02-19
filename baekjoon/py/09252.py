# 변수 세팅
one = " " + input()
two = " " + input()
board = [[0] * len(two) for i in range(len(one))]
ma = 0

# lcs 탐색
for i in range(1, len(one)):
    for j in range(1, len(two)):
        if one[i] == two[j]:
            board[i][j] = board[i - 1][j - 1] + 1
            ma = max(ma, board[i][j])
        else:
            board[i][j] = max(board[i - 1][j], board[i][j - 1])

# 최대 길이 출력
print(ma)

# lcs 출력
lcs = ""
i = len(one) - 1
j = len(two) - 1
while board[i][j] != 0:
    now = board[i][j]
    if board[i - 1][j] == now:
        i -= 1
        continue
    if board[i][j - 1] == now:
        j -= 1
        continue
    lcs = one[i] + lcs
    i -= 1
    j -= 1
print(lcs)