# 궁전 그런디수
def cas(x, y):
    i = 0
    while (x >= 3 * 2 ** i) | (y >= 3 * 2 ** i):
        i += 1
    if i == 0:
        grundy = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
        return grundy[x][y]
    k = 3 * 2 ** (i - 1)
    if (k <= x) & (k <= y):
        return cas(x - k, y - k)
    if x < k:
        return k + cas(x, y - k)
    else:
        return k + cas(x - k, y)
    
# 룩 그런디수
def rook(x, y):
    i = 0
    while (x >= 2 * 2 ** i) | (y >= 2 * 2 ** i):
        i += 1
    if i == 0:
        grundy = [[0, 1], [1, 0]]
        return grundy[x][y]
    k = 2 ** i
    if (k <= x) & (k <= y):
        return rook(x - k, y - k)
    if x < k:
        return k + rook(x, y - k)
    else:
        return k + rook(x - k, y)
    
# 비숍 그런디수
def bishop(x, y):
    return min(x, y)

# 나이트 그런디수
def knight(x, y):
    if (x >= 3) & (y >= 3):
        k = min(x // 3, y // 3)
        return knight(x - k * 3, y - k * 3)
    if (x <= 3) & (y <= 3):
        grundy = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]]
        return grundy[x][y]
    return min(x, y)

# 킹 그런디수
def king(x, y):
    if (x >= 2) & (y >= 2):
        k = min(x // 2, y // 2)
        return king(x - k * 2, y - k * 2)
    if x == 0:
        return y % 2
    if y == 0:
        return x % 2
    return (x + y) % 2 + 2

# 라이브러리 세팅
import sys

# 모든 값을 xor
ans = 0
for i in range(int(sys.stdin.readline())):
    com = list(sys.stdin.readline().split())
    c = com[2]
    x = int(com[0])
    y = int(com[1])
    if c == "R":
        ans ^= rook(x, y)
    elif c == "B":
        ans ^= bishop(x, y)
    elif c == "K":
        ans ^= king(x, y)
    elif c == "N":
        ans ^= knight(x, y)
    elif c == "P":
        ans ^= cas(x, y)

# xor값에따라 답 출력
if ans == 0:
    print("cubelover")
else:
    print("koosaga")