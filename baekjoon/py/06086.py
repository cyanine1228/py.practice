# 라이브러리 세팅
from collections import deque
import sys

# 변수 세팅
board = [[0] * 58 for i in range(58)]
n = int(sys.stdin.readline())
for i in range(n):
    a, b, c = sys.stdin.readline().split()
    a = ord(a) - 65
    b = ord(b) - 65
    c = int(c)
    board[a][b] += c
    board[b][a] += c
ans = 0

# 최대유량 탐색
while True:

    # 변수 세팅
    route = [0]
    que = deque([route])
    tr = False

    # 현재 상황에서 Z로 보낼수 있는 루트 탐색(bfs)
    while len(que) != 0:
        for i in range(len(que)):
            k = que.popleft()
            p = k[len(k) - 1]
            for j in range(58):
                if (board[p][j] > 0) & (not(j in k)):
                    que.append(k + [j])
                    if j == 25:
                        route = k + [j]
                        tr = True
                        break
            if tr:
                break
        if tr:
            break

    # Z로 보낼 수 없다면 답출력후 종료
    else:
        print(ans)
        exit(0)

    # 루트 안에있는 용량의 최소값만큼 각 용량을 빼고, 반대 용량에 추가
    ma = 10000000000000
    for i in range(len(route) - 1):
        ma = min(ma, board[route[i]][route[i + 1]])
    for i in range(len(route) - 1):
        board[route[i]][route[i + 1]] -= ma
        board[route[i + 1]][route[i]] += ma
    ans += ma