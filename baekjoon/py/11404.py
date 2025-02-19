# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
board = [[0] * n for i in range(n)]

# 기본 노드 세팅
for m in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    if board[a][b] == 0:
        board[a][b] = c
    else:
        board[a][b] = min(board[a][b], c)

# 플로이드 워셜
for k in range(n):
    for i in range(n):
        if i == k:
            continue
        for j in range(n):
            if (j == k) | (j == i):
                continue
            if board[i][k] * board[k][j] == 0:
                continue
            distance = board[i][k] + board[k][j]
            if board[i][j] == 0:
                board[i][j] = distance
            else:
                board[i][j] = min(board[i][j], distance)

# 답 출력
for i in board:
    print(*i)