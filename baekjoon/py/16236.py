# 라이브러리 세팅
import sys
from collections import deque

# 변수 세팅
n = int(sys.stdin.readline())
board = []
size = 2
result = 0
exp = 0
bx, by = -1, -1
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            bx = i
            by = j

# 이동(bfs)을 시행할 복제된 보드 생성(0 : 지나갈 수 있음, 1 : 이미 지난 칸, 2 : 먹이 위치, 3 : 벽 위치)
def copyboard():
    moveboard = [[1] * (n + 2) for i in range(n + 2)]
    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                moveboard[i + 1][j + 1] = 1
                x = i
                y = j
            elif 0 < board[i][j] < size:
                moveboard[i + 1][j + 1] = 2
            elif size < board[i][j]:
                moveboard[i + 1][j + 1] = 3
            else:
                moveboard[i + 1][j + 1] = 0
    return moveboard, x + 1, y + 1

# 이동가능 여부 판별후 이동가능하면 그 좌표를, 아니라면 답을 출력한다
def move():
    
    # 변수 세팅
    moveboard, x, y = copyboard()
    que = deque([[x, y]])
    time = 0

    # 가능한 이동이 있는동안
    while len(que) != 0:

        # 이번 이동에 사용한 시간 +1
        time += 1

        # 이동가능 여부 & 이동가능 좌표
        tr = False
        ans = []

        # 경우의 수 탐색
        for _ in range(len(que)):

            # 아래칸
            x, y = que.popleft()
            if moveboard[x + 1][y] == 0:
                que.append([x + 1, y])
                moveboard[x + 1][y] = 1
            elif moveboard[x + 1][y] == 2:
                ans.append([x + 1, y])
                tr = True

            # 위칸
            if moveboard[x - 1][y] == 0:
                que.append([x - 1, y])
                moveboard[x - 1][y] = 1
            elif moveboard[x - 1][y] == 2:
                ans.append([x - 1, y])
                tr = True

            # 오른쪽칸
            if moveboard[x][y + 1] == 0:
                que.append([x, y + 1])
                moveboard[x][y + 1] = 1
            elif moveboard[x][y + 1] == 2:
                ans.append([x, y + 1])
                tr = True

            # 왼쪽 칸
            if moveboard[x][y - 1] == 0:
                que.append([x, y - 1])
                moveboard[x][y - 1] = 1
            elif moveboard[x][y - 1] == 2:
                ans.append([x, y - 1])
                tr = True
        
        # 이동 가능하다면 result 업데이트후 이동가능한 좌표를 정렬후 가장 위, 왼쪽에 있는 값을 반환
        if tr:
            ans.sort(key = lambda x:(x[0], x[1]))
            global result
            result += time
            return ans[0][0] - 1, ans[0][1] - 1

    # 이동 불가능하다면 답 출력후 종료
    print(result)
    exit(0)

# 무한반복
while True:
    
    # 이후 위치 입력
    ax, ay = move()

    # 물고기 위치 변경
    board[ax][ay] = 9
    board[bx][by] = 0
    bx = ax
    by = ay

    # 레벨업
    exp += 1
    if exp == size:
        exp = 0
        size += 1
