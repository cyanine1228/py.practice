# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
hor_board = []
ver_board = ["" for i in range(m)]
for i in range(n):
    k = sys.stdin.readline().strip()
    hor_board.append(k)
    for j in range(len(k)):
        ver_board[j] += k[j]

# 가로판자, 세로판자수 각각 세기
ans = 0
for i in range(n):
    k = hor_board[i].split("|")
    for j in range(len(k)):
        if k[j] != "":
            ans += 1
for i in range(m):
    k = ver_board[i].split("-")
    for j in range(len(k)):
        if k[j] != "":
            ans += 1

# 답 출력
print(ans)