# 라이브러리 세팅
import sys

# 기본 변수, 클래스 세팅
r, c, m = map(int, sys.stdin.readline().split())
position = 0
result = 0
class fish:
    board = [[[] for i in range(c)] for j in range(r)]
    def __init__(self, x, y, v, d, size, n):
        self.x = x
        self.y = y
        self.v = v
        self.d = d
        self.size = size
        self.n = n
        self.survive = 1
        fish.board[x][y].append(n)
a = []
for i in range(m):
    x, y, v, d, size = map(int, sys.stdin.readline().split())
    a.append(fish(x - 1, y - 1, v, d, size, i))

# 낚시 함수(현재 position좌표에서 낚시)
def fishing():
    global result
    for i in range(r):
        if len(fish.board[i][position]) == 1:
            n = fish.board[i][position].pop()
            a[n].survive = 0
            result += a[n].size
            return
        
# 이동(n번째 물고기를 이동)
def move(n):
    x = a[n].x
    y = a[n].y
    d = a[n].d
    distance = a[n].v
    fish.board[x][y].remove(n)
    while True:
        if d == 4:
            if distance <= y:
                y = y - distance
                break
            distance -= y
            y = 0
            d = 3
        elif d == 3:
            if distance < c - y:
                y = y + distance
                break
            distance -= c - y - 1
            y = c - 1
            d = 4
        elif d == 2:
            if distance < r - x:
                x = x + distance
                break
            distance -= r - x - 1
            x = r - 1
            d = 1
        else:
            if distance <= x:
                x = x - distance
                break
            distance -= x
            x = 0
            d = 2
    a[n].x = x
    a[n].y = y
    a[n].d = d
    fish.board[x][y].append(n)

# 포식함수(같은칸에 두마리이상의 물고기가 있는경우 포식)
def eat():
    for i in range(r):
        for j in range(c):
            fish.board[i][j].sort(key = lambda x:-a[x].size)
            while len(fish.board[i][j]) >= 2:
                a[fish.board[i][j].pop()].survive = 0

# 모든 열을 순회할동안 반복
for i in range(c):

    # 낚시후 이동(처음 시작시 이미 한번 이동했다고 가정했기에 둘의 순서를 변경)
    fishing()
    position += 1 

    # 모든 물고기를 이동
    for i in range(m):
        if a[i].survive == 1:
            move(i)

    # 포식
    eat()

# 답 출력
print(result)