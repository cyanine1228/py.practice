# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
ma = 0

# 모든 경우의수 탐색
for i in range(n):
    for j in range(m - 3):
        ma = max(ma, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3])
for i in range(n - 3):
    for j in range(m):
        ma = max(ma, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j])
for i in range(n - 1):
    for j in range(m - 1):
        ma = max(ma, board[i][j] + board[i + 1][j] + board[i][j + 1] + board[i + 1][j + 1])
for i in range(n - 1):
    for j in range(m - 2):
        ma = max(ma, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j])
        ma = max(ma, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 1])
        ma = max(ma, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 2])
        ma = max(ma, board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2] + board[i][j])
        ma = max(ma, board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2] + board[i][j + 1])
        ma = max(ma, board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2] + board[i][j + 2])
        ma = max(ma, board[i + 1][j] + board[i + 1][j + 1] + board[i][j + 2] + board[i][j + 1])
        ma = max(ma, board[i + 1][j + 2] + board[i + 1][j + 1] + board[i][j + 1] + board[i][j])
for i in range(n - 2):
    for j in range(m - 1):
        ma = max(ma, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i][j + 1])
        ma = max(ma, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 1][j + 1])
        ma = max(ma, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j + 1])
        ma = max(ma, board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1] + board[i][j])
        ma = max(ma, board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1] + board[i + 1][j])
        ma = max(ma, board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1] + board[i + 2][j])
        ma = max(ma, board[i + 2][j + 1] + board[i + 1][j + 1] + board[i + 1][j] + board[i][j])
        ma = max(ma, board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j] + board[i + 2][j])

# 답 출력
print(ma)