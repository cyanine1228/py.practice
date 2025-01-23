# 라이브러리 세팅
import sys

# 기본 변수 세팅
n, m, k = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))
word = list(sys.stdin.readline().strip())
board_now = [[0] * m for i in range(n)]                 # 단어의 count번째 글자자까지 가는 경우의수를 저장하기 위한 배열
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            board_now[i][j] = 1
count = 1

# 실행
while count < len(word):

    # 현재 글자에서 다음 글자까지 가는 경우의수를 저장하기 위한 배열
    # 현재 word가 "break", count가 1, 이라면 board_next[2][1]은 board_now[3][1]에서 이동하는 수밖에 없으므로
    # 1을 저장하는 형식으로 작동
    board_next = [[0] * m for i in range(n)]

    # board_next에 값을 넣어주는 작업업
    for i in range(n):
        for j in range(m):
            if board[i][j] == word[count]:
                for l in range(1, k + 1):
                    if i - l >= 0:
                        board_next[i][j] += board_now[i - l][j]
                    if j - l >= 0:
                        board_next[i][j] += board_now[i][j - l]
                    if i + l < n:
                        board_next[i][j] += board_now[i + l][j]
                    if j + l < m:
                        board_next[i][j] += board_now[i][j + l]
    
    # 카운트를 하나 올리고 board_now를 board_next로 바꿈으로써 다음 실행을 준비함
    count += 1
    board_now = list(board_next)

# board_now의 모든 값을 더한것이 모든 경우의 수이므로 그에따라 출력
sum = 0
for i in range(n):
    for j in range(m):
        sum += board_now[i][j]
print(sum)