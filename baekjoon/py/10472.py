# 라이브러리 세팅
import sys

# 테스트 케이스 수 입력
for P in range(int(sys.stdin.readline())):

    # 변수 세팅
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    target = []
    empty_if = True
    for i in range(3):
        k = list(sys.stdin.readline().strip())
        for j in range(3):
            if k[j] == "*":
                empty_if = False
                k[j] = 1
            else:
                k[j] = 0
        target.append(k)
    if empty_if:
        print(0)
        continue
    sum = 0
    ans = 10
    vi = [False] * 9

    # k번째 칸 클릭 함수
    def change(k):
        global ans
        x = k // 3
        y = k % 3
        board[x][y] = 1 - board[x][y]
        if x > 0:
            board[x - 1][y] = 1 - board[x - 1][y]
        if y > 0:
            board[x][y - 1] = 1 - board[x][y - 1]
        if x < 2:
            board[x + 1][y] = 1 - board[x + 1][y]
        if y < 2:
            board[x][y + 1] = 1 - board[x][y + 1]
        tr = True
        for i in range(3):
            for j in range(3):
                if board[i][j] != target[i][j]:
                    tr = False
        if tr:
            ans = min(ans, sum)

    # 모든 경우의수를 탐색하는 함수
    def find(l):
        global sum
        for i in range(l, 9):
            if vi[i]:
                continue
            vi[i] = True
            sum += 1
            change(i)
            find(i + 1)
            change(i)
            sum -= 1
            vi[i] = False

    # 탐색, 답출력
    find(0)
    print(ans)