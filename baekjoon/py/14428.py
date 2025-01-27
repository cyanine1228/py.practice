# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
seg = [[10000000000, -1] for i in range (n * 4)]

# 1번쿼리
def segmodify(s, e, n, i, p):
    if s == e:
        if s == i:
            seg[n] =  [p, s]
            return
        else:
            return
    if s <= i <= e:
        segmodify(s, (s + e) // 2, n * 2, i, p)
        segmodify((s + e) // 2 + 1, e, n * 2 + 1, i, p)
        if seg[n * 2][0] <= seg[n * 2 + 1][0]:
            seg[n] = seg[n * 2]
        else:
            seg[n] = seg[n * 2 + 1]
        return
    return

# 2번쿼리
def findmin(s, e, n, a, b):
    if a <= s <= e <= b:
        return seg[n]
    if (a > e) | (b < s):
        return 100000000000, -1
    P = list(findmin(s, (s + e) // 2, n * 2, a, b))
    Q = list(findmin((s + e) // 2 + 1, e, n * 2 + 1, a, b))
    if P[0] <= Q[0]:
        return P
    return Q
    
# 세그먼트 트리 생성
first = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    segmodify(1, n, 1, i + 1, first[i])

# 쿼리 수행
m = int(sys.stdin.readline())
for M in range(m):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        segmodify(1, n, 1, com[1], com[2])
    else:
        print(findmin(1, n, 1, com[1], com[2])[1])