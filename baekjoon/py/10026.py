# 라이브러리 세팅
import sys

# 재귀 제한 세팅
sys.setrecursionlimit(20000)

# 변수 세팅
n = int(sys.stdin.readline())
normal_board = []
rg_board = []
for i in range(n):
    inp = list(sys.stdin.readline().strip())
    normal_board_one = []
    rg_board_one = []
    for j in range(n):
        if inp[j] == "R":
            normal_board_one.append(1)
            rg_board_one.append(1)
        elif inp[j] == "G":
            normal_board_one.append(2)
            rg_board_one.append(1)
        else:
            normal_board_one.append(3)
            rg_board_one.append(2)
    normal_board.append(normal_board_one)
    rg_board.append(rg_board_one)

# x, y좌표에서 board_type(적록색약 여부)에따른 색깔 반환
def check(x, y, board_type):
    if (x < 0) | (y < 0) | (x >= n) | (y >= n):
        return 0
    if board_type == 0:
        return normal_board[x][y]
    return rg_board[x][y]

# x, y좌표의 값을 제거, 인접한 같은색의 칸도 전부 제거(DFS)
def remove(x, y, color, board_type):
    if board_type == 0:
        normal_board[x][y] = 0
    else:
        rg_board[x][y] = 0
    if check(x, y + 1, board_type) == color:
        remove(x, y + 1, color, board_type)
    if check(x, y - 1, board_type) == color:
        remove(x, y - 1, color, board_type)
    if check(x + 1, y, board_type) == color:
        remove(x + 1, y, color, board_type)
    if check(x - 1, y, board_type) == color:
        remove(x - 1, y, color, board_type)

# 답 탐색
normal_ans = 0
rg_ans = 0
for i in range(n):
    for j in range(n):
        if normal_board[i][j] != 0:
            normal_ans += 1
            remove(i, j, normal_board[i][j], 0)
        if rg_board[i][j] != 0:
            rg_ans += 1
            remove(i, j, rg_board[i][j], 1)
        
# 답 출력
print(normal_ans, rg_ans)