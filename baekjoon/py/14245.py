# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
seg = [[0, 0] for i in range(n * 4)]

# 레이지 전파 함수
def lazy(s, e, n):
    l = seg[n][1]
    seg[n][1] = 0
    if s != e:
        seg[n * 2][1] ^= l
        seg[n * 2 + 1][1] ^= l
    else:
        seg[n][0] ^= l

# 값 수정 함수
def modify(s, e, n, p, q, l):
    lazy(s, e, n)
    if p <= s <= e <= q:
        if s == e:
            seg[n][0] ^= l
        else:
            seg[n * 2][1] ^= l
            seg[n * 2 + 1][1] ^= l
        return
    if (e < p) | (s > q):
        return
    modify(s, (s + e) // 2, n * 2, p, q, l)
    modify((s + e) // 2 + 1, e, n * 2 + 1, p, q, l)

# 탐색 함수
def find(s, e, n, p):
    lazy(s, e, n)
    if s == e == p:
        return seg[n][0]
    if (e < p) | (s > p):
        return 0
    a = find(s, (s + e) // 2, n * 2, p)
    b = find((s + e) // 2 + 1, e, n * 2 + 1, p)
    return a + b

# 세그먼트트리 생성
first = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    modify(1, n, 1, i + 1, i + 1, first[i])

# 쿼리 수행
for i in range(int(sys.stdin.readline())):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        modify(1, n, 1, com[1] + 1, com[2] + 1, com[3])
    else:
        print(find(1, n, 1, com[1] + 1))