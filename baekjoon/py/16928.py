# 라이브러리 세팅
from collections import deque
import sys

# 변수 세팅
board = [None] + [0] + [None] * 105
que = deque([1])
n, m = map(int, sys.stdin.readline().split())
ladder = []
snake = []
for N in range(n):
    ladder.append(list(map(int, sys.stdin.readline().split())))
for M in range(m):
    snake.append(list(map(int, sys.stdin.readline().split())))

# bfs 실행
time = 0
while True:
    time += 1
    for i in range(len(que)):
        k = que.popleft()
        for j in range(1, 7):
            next = k + j
            tr = True
            for l in ladder:
                if l[0] == next:
                    tr = False
                    if l[1] == 100:
                            print(time)
                            exit(0)
                    if board[l[1]] == None:
                        board[l[1]] = time
                        que.append(l[1])
                    break
            for l in snake:
                if l[0] == next:
                    tr = False
                    if l[1] == 100:
                            print(time)
                            exit(0)
                    if board[l[1]] == None:
                        board[l[1]] = time
                        que.append(l[1])
                    break
            if tr:
                if next == 100:
                            print(time)
                            exit(0)
                if board[next] == None:
                    board[next] = time
                    que.append(next)