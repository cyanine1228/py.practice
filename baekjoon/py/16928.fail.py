# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())   
board = [0] * 106
up = {}
uplist = set()

# 사다리 세팅
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    uplist.add(a)
    up[a] = b

# 뱀 세팅
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a + 5] = 100000000000

# 1번째 칸부터 100번째 칸까지 올라가며 최소 행동 수를 저장
for i in range(7, 106):
    
    # 만약 이미 저장된 숫자가 있다면(사다리로 올라갔거나, 뱀때문에 내려가는 자리) 스킵
    if board[i] != 0:
        continue

    # 현재 칸으로 가기까지의 최소행동수는 전 여섯칸의 최소행동수의 최소값 + 1
    board[i] = min(board[i - 1], board[i - 2], board[i - 3], board[i - 4], board[i - 5], board[i - 6]) + 1
    
    # 만약 현재칸이 사다리의 아래쪽이라면 사다리 위쪽을 같은 행동수로 저장
    if i - 5 in uplist:
        board[up[i - 5] + 5] = board[i]

# 100번째칸의 최소행동수 출력
print(board[105])
