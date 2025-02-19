# 라이브러리 세팅
import sys

# 기본 변수 세팅
n = int(sys.stdin.readline())
seg = [[0, [1, 0, None]] for i in range(n * 4)]
mod = 1000000007

# 레이지 전파 함수
def lazy(s, e, n):
    k = list(seg[n][1])
    seg[n][1] = [1, 0, None]
    if k[2] != None:
        seg[n][0] = k[2] * (e - s + 1)
    seg[n][0] = (seg[n][0] * k[0] + k[1] * (e - s + 1)) % mod
    if s != e:
        if k[2] != None:
            seg[n * 2][1] = list(k)
            seg[n * 2 + 1][1] = list(k)
        else:
            if seg[n * 2][1][2] != None:
                seg[n * 2][1][0] = seg[n * 2][1][0] * k[0] % mod
                seg[n * 2][1][1] = (seg[n * 2][1][1] * k[0] + k[1]) % mod
            else:
                seg[n * 2][1] = [seg[n * 2][1][0] * k[0] % mod, (seg[n * 2][1][1] * k[0] + k[1]) % mod, None]
            if seg[n * 2 + 1][1][2] != None:
                seg[n * 2 + 1][1][0] = seg[n * 2 + 1][1][0] * k[0] % mod
                seg[n * 2 + 1][1][1] = (seg[n * 2 + 1][1][1] * k[0] + k[1]) % mod          
            else:
                seg[n * 2 + 1][1] = [seg[n * 2 + 1][1][0] * k[0] % mod, (seg[n * 2 + 1][1][1] * k[0] + k[1]) % mod, None]

# 1번 쿼리
def modify1(s, e, n, x, y, v):
    lazy(s, e, n)
    if x <= s <= e <= y:
        seg[n][0] = (seg[n][0] + v * (e - s + 1)) % mod
        if s != e:
            seg[n * 2][1][1] = (seg[n * 2][1][1] + v) % mod
            seg[n * 2 + 1][1][1] = (seg[n * 2 + 1][1][1] + v) % mod
        return
    if (x > e) | (y < s):
        return
    modify1(s, (s + e) // 2, n * 2, x, y, v)
    modify1((s + e) // 2 + 1, e, n * 2 + 1, x, y, v)
    seg[n][0] = (seg[n * 2][0] + seg[n * 2 + 1][0]) % mod
    return

# 2번 쿼리
def modify2(s, e, n, x, y, v):
    lazy(s, e, n)
    if x <= s <= e <= y:
        seg[n][0] = (seg[n][0] * v) % mod
        if s != e:
            seg[n * 2][1][0] = (seg[n * 2][1][0] * v) % mod
            seg[n * 2][1][1] = (seg[n * 2][1][1] * v) % mod
            seg[n * 2 + 1][1][0] = (seg[n * 2 + 1][1][0] * v) % mod
            seg[n * 2 + 1][1][1] = (seg[n * 2 + 1][1][1] * v) % mod
        return
    if (x > e) | (y < s):
        return
    modify2(s, (s + e) // 2, n * 2, x, y, v)
    modify2((s + e) // 2 + 1, e, n * 2 + 1, x, y, v)
    seg[n][0] = (seg[n * 2][0] + seg[n * 2 + 1][0]) % mod
    return

# 3번 쿼리
def modify3(s, e, n, x, y, v):
    lazy(s, e, n)
    if x <= s <= e <= y:
        seg[n][0] = v * (e - s + 1)
        if s != e:
            seg[n * 2][1] = [1, 0, v]
            seg[n * 2 + 1][1] = [1, 0, v]
        return
    if (x > e) | (y < s):
        return
    modify3(s, (s + e) // 2, n * 2, x, y, v)
    modify3((s + e) // 2 + 1, e, n * 2 + 1, x, y, v)
    seg[n][0] = (seg[n * 2][0] + seg[n * 2 + 1][0]) % mod
    return

# 4번 쿼리
def find(s, e, n, x, y):
    lazy(s, e, n)
    if x <= s <= e <= y:
        return seg[n][0] % mod
    if (x > e) | (y < s):
        return 0
    a = find(s, (s + e) // 2, n * 2, x, y)
    b = find((s + e) // 2 + 1, e, n * 2 + 1, x, y)
    return (a + b) % mod

# 세그 초기화
a = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    modify3(1, n, 1, i + 1, i + 1, a[i])

# 쿼리 수행
for M in range(int(sys.stdin.readline())):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        modify1(1, n, 1, com[1], com[2], com[3])
    elif com[0] == 2:
        modify2(1, n, 1, com[1], com[2], com[3])
    elif com[0] == 3:
        modify3(1, n, 1, com[1], com[2], com[3])
    else:
        print(find(1, n, 1, com[1], com[2]))