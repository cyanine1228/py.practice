# 라이브러리 세팅 
import sys
from collections import deque

# 변수 세팅 
n, m = map(int, sys.stdin.readline().split())
board = [["W"] * (m + 2)]
for i in range(n):
    board.append(["W"] + list(sys.stdin.readline().strip()) + ["W"])
board.append(["W"] * (m + 2))
ma = 0

# 모든 칸을 순회
for i in range(1, n + 1):
    for j in range(1, m + 1):

        # x, y좌표 육지로부터 가장 먼 육지의 거리를 반환하는 함수
        def find(x, y):
            que = deque([[x, y]])
            t = -1
            board[x][y] = "T"
            while len(que) != 0:
                t += 1
                for _ in range(len(que)):
                    k = que.popleft()
                    x = k[0]
                    y = k[1]
                    if board[x + 1][y] == "L":
                        board[x + 1][y] = "T"
                        que.append([x + 1, y])
                    if board[x - 1][y] == "L":
                        board[x - 1][y] = "T"
                        que.append([x - 1, y])
                    if board[x][y + 1] == "L":
                        board[x][y + 1] = "T"
                        que.append([x, y + 1])
                    if board[x][y - 1] == "L":
                        board[x][y - 1] = "T"
                        que.append([x, y - 1])
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if board[i][j] == "T":
                        board[i][j] = "L"
            return t
        
        # 모든 육지에대해 ma갱신 시도
        if board[i][j] == "L":
            ma = max(ma, find(i, j))

# ma출력
print(ma)