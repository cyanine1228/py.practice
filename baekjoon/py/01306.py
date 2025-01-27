# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))
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
        seg[n] = max(seg[n], p)
        segmodify(s, (s + e) // 2, n * 2, i, p)
        segmodify((s + e) // 2 + 1, e, n * 2 + 1, i, p)
        return
    
# 세그먼트트리 최대값 탐색 함수
def findmax(s, e, n, a, b):
    if a <= s <= e <= b:
        return seg[n]
    if (s > b) | (e < a):
        return 0
    return max(findmax(s, (s + e) // 2, n * 2, a, b), findmax((s + e) // 2 + 1, e, n * 2 + 1, a, b))

# 세그먼트트리 세팅
for i in range(n):
    segmodify(1, n, 1, i + 1, x[i])

# 답 출력
for k in range(m, n - m + 2):
    print(findmax(1, n, 1, k - (m - 1), k + (m - 1)), end = " ")