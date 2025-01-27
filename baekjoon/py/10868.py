# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
seg = [10000000000 for i in range(262144)]

# 함수 세팅
def segmodify(s, e, n, i, p):       # 세그먼트트리 수정 함수
    if s == e == i:
        seg[n] = p
        return
    elif s == e:
        return
    if s <= i <= e:
        seg[n] = min(seg[n], p)
        segmodify(s, (s + e) // 2, n * 2, i, p)
        segmodify((s + e) // 2 + 1, e, n * 2 + 1, i, p)

def findmin(s, e, n, a, b):         # 최소값 탐색 함수
    if a <= s <= e <= b:
        return seg[n]
    if e < a:
        return 1000000000000
    if s > b:
        return 1000000000000
    return min(findmin(s, (s + e) // 2, n * 2, a, b), findmin((s + e) // 2 + 1, e, n * 2 + 1, a, b))

# 세그먼트 트리 제작
for i in range(1, n + 1):
    segmodify(1, n, 1, i, int(sys.stdin.readline()))

# 답 출력
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(findmin(1, n, 1, a, b))