# 라이브러리 세팅
import sys

# 재귀깊이 세팅
sys.setrecursionlimit(20000)

# 변수 세팅
n, m, k = map(int, sys.stdin.readline().split())
board = [[0] * (m + 2) for i in range(n + 2)]
for K in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x][y] = 1

# x, y좌표를 포함하는 쓰레기가 존재한다면 제거, 크기를 반환
def remov(x, y):
    if board[x][y] == 0:
        return 0
    board[x][y] = 0
    a = remov(x + 1, y)
    b = remov(x - 1, y)
    c = remov(x, y + 1)
    d = remov(x, y - 1)
    return 1 + a + b + c + d

# 모든 위치를 순회하며 ma 갱신
ma = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ma = max(ma, remov(i, j))

# 출력
print(ma)