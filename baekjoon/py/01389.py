# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
board = [[0] * n for i in range(n)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    board[x][y] = 1
    board[y][x] = 1

# 플로이드 워셜
for i in range(n):
    for p in range(n):
        if p == i:
            continue
        for q in range(n):
            if q == i:
                continue
            if p == q:
                continue
            if (board[p][i] != 0) & (board[i][q] != 0):
                if board[p][q] == 0:
                    board[p][q] = board[p][i] + board[i][q]
                else:
                    board[p][q] = min(board[p][q], board[p][i] + board[i][q])

# 답 갱신
ans = 1000000000000
ansnum = -1
for i in range(len(board)):
    sum = 0
    for j in board[i]:
        sum += j
    if ans > sum:
        ans = sum
        ansnum = i + 1

# 답 출력
print(ansnum)