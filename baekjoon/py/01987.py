# 라이브러리 세팅
import sys

# 기초 변수 세팅
r, c = map(int, sys.stdin.readline().split())
board = []
for i in range(r):
    board.append(list(sys.stdin.readline().strip())) 
s = {board[0][0]}
x, y = 0, 0
ma = 0

# dfs 함수 구현
def dfs(x, y):

    # 만약 현재까지 지나온칸이 역대 최고칸보다 많다면 갱신
    global ma
    if len(s) > ma:
        ma = len(s)

    # 상하좌우로 이동이 가능한지 판별후 이동
    if (x + 1 < r):
        if (not(board[x + 1][y] in s)):
            s.add(board[x + 1][y])
            dfs(x + 1, y)
            s.remove(board[x + 1][y])
    if (x - 1 >= 0):
        if (not(board[x - 1][y] in s)):
            s.add(board[x - 1][y])
            dfs(x - 1, y)
            s.remove(board[x - 1][y])
    if (y + 1 < c):
        if (not(board[x][y + 1] in s)):
            s.add(board[x][y + 1])
            dfs(x, y + 1) 
            s.remove(board[x][y + 1])
    if (y - 1 >= 0):
        if (not(board[x][y - 1] in s)):
            s.add(board[x][y - 1])
            dfs(x, y - 1)
            s.remove(board[x][y - 1])

# 함수 실행후 결과 출력
dfs(x, y)
print(ma)