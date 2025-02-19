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
