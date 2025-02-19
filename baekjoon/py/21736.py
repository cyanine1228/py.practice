# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
board = []
table = [[1, 0], [-1, 0], [0, 1], [0, -1]]
sx, sy = -1, -1
for i in range(n):
    inp = list(sys.stdin.readline().strip())
    for j in range(m):
        if inp[j] == "O":
            inp[j] = 0
        elif inp[j] == "I":
            inp[j] = 1
            sx, sy = i, j
        elif inp[j] == "P":
            inp[j] = 2
        else:
            inp[j] = -1
    board.append(inp)
stack = [[sx, sy]]
ans = 0

# x, y좌표에 갈수없다면 0, 갈 수 있다면 1, 사람이 있다면 2반환
def move(x, y):
    if x < 0:
        return 0
    if y < 0:
        return 0
    if x == n:
        return 0
    if y == m:
        return 0
    if board[x][y] == -1:
        return 0
    if board[x][y] == 1:
        return 0
    if board[x][y] == 0:
        return 1
    if board[x][y] == 2:
        return 2
    
# dfs를 통해 이동가능한 모든칸 탐색
while len(stack) != 0:

    # 스택에서 좌표 하나를 추출
    k = stack.pop()

    # 추출한 좌표의 전후좌우를 조사
    for i in range(4):
        lx, ly = k[0] + table[i][0], k[1] + table[i][1]
        if move(lx, ly) == 1:
            stack.append([lx, ly])
            board[lx][ly] = 1
        elif move(lx, ly) == 2:
            stack.append([lx, ly])
            board[lx][ly] = 1
            ans += 1

# 답 출력
if ans == 0:
    print("TT")
else:
    print(ans)