# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

# 플로이드 워셜
for i in range(n):
    for p in range(n):
        for q in range(n):
            if (board[p][i] == 1) & (board[i][q] == 1):
                board[p][q] = 1

# 답 출력
for i in range(n):
    print(*board[i])