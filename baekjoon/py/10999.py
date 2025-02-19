# 라이브러리 세팅
import sys

# 변수 세팅
n, m, k = map(int, sys.stdin.readline().split())
seg = [[0, 0] for i in range(n * 4)]

# 레이지 전파 함수
def lazy(s, e, n):
    l = seg[n][1]
    seg[n][1] = 0
    seg[n][0] += (e - s + 1) * l
    if s != e:
        seg[n * 2][1] += l
        seg[n * 2 + 1][1] += l

# 값 수정 함수
def modify(s, e, n, p, q, l):
    lazy(s, e, n)
    if p <= s <= e <= q:
        seg[n][0] += (e - s + 1) * l
        if s != e:
            seg[n * 2][1] += l
            seg[n * 2 + 1][1] += l
        return seg[n][0]
    if (e < p) | (s > q):
        return 0
    modify(s, (s + e) // 2, n * 2, p, q, l)
    modify((s + e) // 2 + 1, e, n * 2 + 1, p, q, l)
    seg[n][0] = seg[n * 2][0] + seg[n * 2 + 1][0]
    return seg[n][0]

# 구간합 탐색 함수
def find(s, e, n, p, q):
    lazy(s, e, n)
    if p <= s <= e <= q:
        return seg[n][0]
    if (e < p) | (s > q):
        return 0
    a = find(s, (s + e) // 2, n * 2, p, q)
    b = find((s + e) // 2 + 1, e, n * 2 + 1, p, q)
    return a + b

# 세그먼트트리 생성
for i in range(1, n + 1):
    l = int(sys.stdin.readline())
    modify(1, n, 1, i, i, l)

# 쿼리 수행
for i in range(m + k):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        modify(1, n, 1, com[1], com[2], com[3])
    else:
        print(find(1, n, 1, com[1], com[2]))