# 라이브러리 세팅
import sys

# 기본 변수 선언
n = int(sys.stdin.readline())
board = list(map(int, sys.stdin.readline().split()))
ans = 0
now = 0
nownum = board[0]

# 보드 탐색
for i in range(1, len(board)):

    # 현재 탐색중인 값보다 역대 최고 높이가 더 크다면
    if board[i] < nownum:
        now += 1                # 현재 킬수에 1 추가
        if ans < now:           # 최고킬보다 많다면
            ans = now           # 최고킬 갱신

    # 역대 최고높이가 갱신된다면
    else:
        nownum = board[i]       # 최고높이 갱신
        now = 0                 # 현재킬 갱신

# 답 출력
print(ans)