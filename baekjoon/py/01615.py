# 라이브러리 세팅
import sys
n, m = map(int, sys.stdin.readline().split())
line = [[] for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
for i in range(n + 1):
    line[i].sort()
seg = [0] * (4096)
ans = 0

# 배열 p번째 값에 +1을 하는 함수(세그먼트 트리)
def segplus(s, e, n, p):
    if s == e == p:
        seg[n] += 1 
        return
    if s <= p <= e:
        seg[n] += 1
        segplus(s, (s + e) // 2, n * 2, p)
        segplus((s + e) // 2 + 1, e, n * 2 + 1, p)
        return
    return

# 배열 p ~ q구간의 구간합을 구하는 함수
def segsum(s, e, p, q, n):
    if p <= s == e <= q:
        return seg[n]
    if (s > q) | (e < p):
        return 0
    if p <= s <= e <= q:
        return seg[n]
    return segsum(s, (s + e) // 2, p, q, n * 2) + segsum((s + e) // 2 + 1, e, p, q, n * 2 + 1)

# 실제 실행
for i in line:
    for j in i:
        ans += segsum(1, n, j + 1, n, 1)
        segplus(1, n, 1, j)

# 답 출력
print(ans)