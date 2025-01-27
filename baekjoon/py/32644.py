# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
seg = [0] * (n * 4)

# 세그먼트트리 변경 함수
def segmodify(s, e, n, i, p):
    if s == e:
        if s == i:
            seg[n] = p
            return
        else:
            return
    if s <= i <= e:
        segmodify(s, (s + e) // 2, n * 2, i, p)
        segmodify((s + e) // 2 + 1, e, n * 2 + 1, i, p)
        seg[n] = seg[n * 2] + seg[n * 2 + 1]

# 세그먼트트리 구간합 함수
def segsum(s, e, n, a, b):
    if a <= s <= e <= b:
        return seg[n]
    if (s > b) | (e < a):
        return 0
    return segsum(s, (s + e) // 2, n * 2, a, b) + segsum((s + e) // 2 + 1, e, n * 2 + 1, a, b)

# 세그먼트트리 생성
p = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    segmodify(1, n, 1, i + 1, p[i])

# 답 출력
k = list(map(int, sys.stdin.readline().split()))
for i in k:
    print(segsum(1, n, 1, 1, i - 1) + 1, end = " ")
    segmodify(1, n, 1, i, 0)