# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
if n == 1:
    print(input())
    exit(0)
board = (1 << ((n * 2 - 1) ** 2)) - 1
line1 = (1 << (n * 2 - 1)) - 1
line2 = 1
for i in range(n * 2 - 2):
    line2 = 1 + (line2 << (n * 2 - 1))
for i in range(n - 1, -1, -1):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if line[j] == 0:
            continue
        board &= ~(1 << ((n * 2 - 1) * (i + j) + (n - 1 - i + j)))
ma = 0
sum = 0

# 같은 색의 칸내에 들어갈 수 있는 비숍의 최대수를 구하는 함수
def dfs(l):
    global sum
    global ma
    global board
    if sum == n * 2 - 2:
        print(sum)
        exit(0)
    if sum > ma:
        ma = sum
    for p in range(l, (n * 2 - 1), 2):
        for q in range((n * 2 - 1)):
            k = p * (n * 2 - 1) + q
            if board & (1 << k) != 0:
                continue
            i = k // (n * 2 - 1)
            j = k % (n * 2 - 1)
            past = board
            sum += 1
            board |= (line1 << (i * (n * 2 - 1)))
            board |= (line2 << j)
            dfs(p)
            sum -= 1
            board = past

# 한가지 색에서 실행
dfs(0)
ma1 = ma

# 변수 초기화
ma = 0
sum = 0

# 다른색에서 실행
dfs(1)
ma2 = ma

# 합을 출력
print(ma1 + ma2)
