# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
seg = [[0, 0] for i in range(n * 4)]

# 레이지 전파 함수
def lazy(s, e, n):
    k = seg[n][1]
    seg[n][1] = 0
    seg[n][0] += (e - s + 1) * k
    if s != e:
        seg[n * 2][1] += k
        seg[n * 2 + 1][1] += k

# 세그먼트 수정 함수
def modify(s, e, n, i, j, k):
    lazy(s, e, n)
    if i <= s <= e <= j:
        seg[n][0] += (e - s + 1) * k
        if s != e:
            seg[n * 2][1] += k
            seg[n * 2 + 1][1] += k
        return
    if (e < i) | (s > j):
        return
    modify(s, (s + e) // 2, n * 2, i, j, k)
    modify((s + e) // 2 + 1, e, n * 2 + 1, i, j, k)
    seg[n][0] = seg[n * 2][0] + seg[n * 2 + 1][0]

# Ax 탐색 함수
def find(s, e, n, x):
    lazy(s, e, n)
    if s == e == x:
        return seg[n][0]
    if not(s <= x <= e):
        return 0
    a = find(s, (s + e) // 2, n * 2, x)
    b = find((s + e) // 2 + 1, e, n * 2 + 1, x)
    return a + b

# 세그먼트트리 초기화
a = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    modify(1, n, 1, i + 1, i + 1, a[i])

# 쿼리 수행
for M in range(int(sys.stdin.readline())):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        modify(1, n, 1, com[1], com[2], com[3])
    else:
        print(find(1, n, 1, com[1]))