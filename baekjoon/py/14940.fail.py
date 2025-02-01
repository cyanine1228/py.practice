# 라이브러리 세팅
import sys
from collections import deque

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
board = [[0] * (m + 2)]
x, y = -1, -1
for i in range(n):
    board.append([0] + list(map(int, sys.stdin.readline().split())) + [0])
    for j in range(1, m + 1):
        if board[i][j] == 2:
            board[i][j] = 0
            x, y = i, j
board.append([0] * (m + 2))
ans = [[0] * m for i in range(n)]
k = 0
que = deque([[x, y]])

# bfs 시행, 더이상 탐색가능 칸이 없다면 종료
while len(que) != 0:
    for _ in range(len(que)):
        i = que.popleft()
        ans[i[0] - 1][i[1] - 1] = k
        if board[i[0] + 1][i[1]] != 0:
            que.append([i[0] + 1, i[1]])
            board[i[0] + 1][i[1]] = 0
        if board[i[0] - 1][i[1]] != 0:
            que.append([i[0] - 1, i[1]])
            board[i[0] - 1][i[1]] = 0
        if board[i[0]][i[1] + 1] != 0:
            que.append([i[0], i[1] + 1])
            board[i[0]][i[1] + 1] = 0
        if board[i[0]][i[1] - 1] != 0:
            que.append([i[0], i[1] - 1])
            board[i[0]][i[1] - 1] = 0
    k += 1

# 답 출력
for i in range(n):
    for j in range(m):
        if board[i + 1][j + 1] == 1:
            print(-1, end = " ")
        else:
            print(ans[i][j], end = " ")
    print("")