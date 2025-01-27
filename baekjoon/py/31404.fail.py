# 라이브러리 세팅
import sys

# 기본 변수 세팅
h, w = map(int, sys.stdin.readline().split())
x, y, rot = map(int, sys.stdin.readline().split())
board = [[1] * w for i in range(h)]
vi = [[{(5, 0)} for i in range(w)] for j in range(h)]
a = []
for i in range(h):
    a.append(list(map(int, list(sys.stdin.readline().strip()))))
b = []
for i in range(h):
    b.append(list(map(int, list(sys.stdin.readline().strip()))))
ans = 0
act = 0
record = [0]

# 시행
while True:
    print(x, y, ans)
    # 현재 좌표에 먼지가 있는 경우
    if board[x][y] == 1:
        record.append(record[len(record) - 1] + 1)
        board[x][y] = 0
        rot = (rot + a[x][y]) % 4
        ans += act
        act = 0

    # 먼지가 없는 경우
    else:

        # 만약에 이미 같은 방식(같은 방향)으로 온적이 있으며 다시 올동안 지운 먼지가 없없는경우 답을 적고 탈출
        for k in vi[x][y]:
            if rot == k[0]:
                if k[1] == record[len(record) - 1]:
                    print(ans + 1)
                    exit(0)
        
        # 현재칸에 방문한 정보(방향, 이동 횟수)를 기입후 B에따라 방향 회전
        vi[x][y].add((rot, record[len(record) - 1]))
        rot = (rot + b[x][y]) % 4
        record.append(record[len(record) - 1])
    
    # 이동, 만약 외부로 벗어난다면 답출력후 탈출
    if rot == 0:
        x -= 1
        act += 1
        if x == -1: 
            print(ans)
            exit(0)
    elif rot == 1:
        y += 1
        act += 1
        if y == w:
            print(ans)
            exit(0)
    elif rot == 2:
        x += 1
        act += 1
        if x == h:
            print(ans)
            exit(0)
    else:
        y -= 1
        act += 1
        if y == -1:
            print(ans)
            exit(0)
