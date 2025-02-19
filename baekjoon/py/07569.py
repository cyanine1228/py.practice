# 라이브러리 세팅
import sys
from collections import deque

# 변수 세팅
m, n, h = map(int, sys.stdin.readline().split())
board = []
table = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
que = deque()
for H in range(h):
    board_one = []
    for N in range(n):
        inp = list(map(int, sys.stdin.readline().split()))
        for M in range(m):
            if inp[M] == 1:
                que.append([H, N, M])
        board_one.append(list(inp))
    board.append(list(board_one))

# 예외 처리(시작하자마자 종료되는 경우)
tr = False
for H in range(h):
    for N in range(n):
        for M in range(m):
            if board[H][N][M] == 0:
                tr = True
                break
        if tr:
            break
    if tr:
        break
else:
    print(0)
    exit(0)

# x, y, z칸이 숙성되지 않은 토마토인지 확인하는 함수
def move_if(x, y, z):
    if (x < 0) | (y < 0) | (z < 0) | (x >= h) | (y >= n) | (z >= m):
        return False 
    if board[x][y][z] == 0:
        return True
    return False

# bfs시행
time = 0
while len(que) != 0:
    for i in range(len(que)):
        k = que.popleft()
        for j in table:
            x, y, z = k[0] + j[0], k[1] + j[1], k[2] + j[2]
            if move_if(x, y, z):
                board[x][y][z] = 1
                que.append([x, y, z])
    time += 1

# bfs시행 후에도 0(익지 않은 토마토)가 남아있다면 -1출력
for H in range(h):
    for N in range(n):
        for M in range(m):
            if board[H][N][M] == 0:
                print(-1)
                exit(0)

# 답 출력
else:
    print(time - 1)