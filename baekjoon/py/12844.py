# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
seg = [[0, 0] for i in range(n * 4)]

# 레이지 전파 함수
def lazy(s, e, n):
    l = seg[n][1]
    seg[n][1] = 0
    seg[n][0] ^= l * (1 - (e - s) % 2)
    if s != e:
        seg[n * 2][1] ^= l
        seg[n * 2 + 1][1] ^= l

# 세그 수정 함수
def modify(s, e, n, i, j, k):
    lazy(s, e, n)
    if i <= s <= e <= j:
        seg[n][0] ^= k * (1 - (e - s) % 2)
        if s != e:
            seg[n * 2][1] ^= k
            seg[n * 2 + 1][1] ^= k
        return seg[n][0]
    if (j < s) | (i > e):
        return seg[n][0]
    seg[n][0] = modify(s, (s + e) // 2, n * 2, i, j, k) ^ modify((s + e) // 2 + 1, e, n * 2 + 1, i, j, k)
    return seg[n][0]

# 세그 탐색 함수
def find(s, e, n, i, j):
    lazy(s, e, n)
    if i <= s <= e <= j:
        return seg[n][0]
    if (j < s) | (i > e):
        return 0
    return find(s, (s + e) // 2, n * 2, i, j) ^ find((s + e) // 2 + 1, e, n * 2 + 1, i, j)

# 세그 초기화
a = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    modify(1, n, 1, i + 1, i + 1, a[i])

# 쿼리 수행
for M in range(int(sys.stdin.readline())):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        modify(1, n, 1, com[1] + 1, com[2] + 1, com[3])
    else:
        print(find(1, n, 1, com[1] + 1, com[2] + 1))