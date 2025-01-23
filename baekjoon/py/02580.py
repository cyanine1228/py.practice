# 라이브러리 세팅
import sys

# 보드 세팅
board = []
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))

# dfs 알고리즘을 이용한 스도쿠 풀이 구현
def dfs():

    # 만약 빈칸이 없다면 보드 출력후 탈출
    tr = True
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                tr = False
                break
    if tr:
        for i in range(9):
            print(*board[i])
        exit(0)

    # 빈칸을 찾아서 풀이 시작
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:

                # 가능한 수 모음(num) 집합 생성성
                num = {1, 2, 3, 4, 5, 6, 7, 8, 9}

                # 같은 가로축, 세로축에 있는 값들을 num에서 제거
                for k in range(9):
                    if board[i][k] in num:
                        num.remove(board[i][k])
                    if board[k][j] in num:
                        num.remove(board[k][j])
                    p = i // 3
                    q = j // 3

                # 같은 3 * 3칸 안에있는 값들을 num에서 제거
                for P in range(p * 3, p * 3 + 3):
                    for Q in range(q * 3, q * 3 + 3):            
                        if board[P][Q] in num:
                            num.remove(board[P][Q])

                # num에 수가 없다면 잘못된 경우이므로 리턴
                if len(num) == 0:
                    return
                
                # num에 있는 값들을 하나하나 넣어보며 재귀를 통해 다음 숫자도 풀이 시작
                for N in num:
                    board[i][j] = N
                    dfs()
                board[i][j] = 0
                return

# 함수 실행
dfs()