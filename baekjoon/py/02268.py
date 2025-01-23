# 라이브러리 세팅
import sys

# 기본 변수 세팅
n, m = map(int, sys.stdin.readline().split())
lis = [0] * (n + 1)
seg = [0 for i in range(n * 4)]

# 값 변경
def segmodify(i, k, n, s, e):
    if s == e == i:
        seg[n] = k
        return
    if s <= i <= e:
        seg[n] += k - lis[i]
        segmodify(i, k, n * 2, s, (s + e) // 2)
        segmodify(i, k, n * 2 + 1, (s + e) // 2 + 1, e)
        return
    return

# 부분합 
def segsum(s, e, n, f, l):
    if s <= f <= l <= e:
        return seg[n]
    if (s > l) | (e < f):
        return 0
    return segsum(s, e, n * 2, f, (f + l) // 2) + segsum(s, e, n * 2 + 1, (f + l) // 2 + 1, l)


# 명령에따른 수정, 출력
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        if b > c:
            t = b
            b = c
            c = t
        print(segsum(b, c, 1, 1, n))
    else:
        segmodify(b, c, 1, 1, n)
        lis[b] = c