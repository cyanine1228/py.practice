# 라이브러리 세팅
import sys

# 누적합 세팅
n, m = map(int, sys.stdin.readline().split())
board = [[0] * (n + 1)]
for i in range(n):
    board_one = [0]
    inp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        board_one.append(board_one[j] + board[i][j + 1] + inp[j] - board[i][j])
    board.append(list(board_one))

# 2차원 누적합을통한 쿼리수행 
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])    