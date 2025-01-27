import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
board = []
rx, ry = -1, -1
bx, by = -1, -1
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            rx = i
            ry = j
        elif board[i][j] == "B":
            bx = i
            by = j
que = deque()
que.append(board)
act = 1
while len(que) != 0:
    for _ in range(len(que)):
        board = que.popleft()
        board2 = list(board)
        if rx < bx:
            while board2[rx - 1][ry] == ".":
                board2[rx][ry] = "."
                board2[rx - 1][ry] = "R"
                rx -= 1
            while board2[bx - 1][by] == ".":
                board2[bx][by] = "."
                board2[bx - 1][by] = "R"
                bx -= 1
        else:
            while board2[bx - 1][by] == ".":
                board2[bx][by] = "."
                board2[bx - 1][by] = "R"
                bx -= 1
            while board2[rx - 1][ry] == ".":
                board2[rx][ry] = "."
                board2[rx - 1][ry] = "R"
                rx -= 1
        que.append(board2)
        print(board2)
        input()