# 라이브러리 세팅 
import sys

# 변수 세팅 
n, m, k = map(int, sys.stdin.readline().split())
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
        seg[n] = seg[n * 2] * seg[n * 2 + 1] % 1000000007

# 세그먼트트리 곱 연산 함수
def segsq(s, e, n, a, b):
    if a <= s <= e <= b:
        return seg[n]
    if (s > b) | (e < a):
        return 1
    return segsq(s, (s + e) // 2, n * 2, a, b) * segsq((s + e) // 2 + 1, e, n * 2 + 1, a, b) % 1000000007

# 세그먼트트리 생성 
for i in range(n):
    segmodify(1, n, 1, i + 1, int(sys.stdin.readline()))

# 명령 수행
for i in range(m + k):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        segmodify(1, n, 1, com[1], com[2])
    else:
        print(segsq(1, n, 1, com[1], com[2]))