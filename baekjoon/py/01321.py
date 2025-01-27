# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
sol = list(map(int, sys.stdin.readline().split()))
seg = [0] * (n * 4)

# 세그먼트트리 변경 함수
def segmodify(s, e, n, i, p):
    if s == e:
        if s == i:
            seg[n] = seg[n] + p
            return
        else:
            return
    if s <= i <= e:
        segmodify(s, (s + e) // 2, n * 2, i, p)
        segmodify((s + e) // 2 + 1, e, n * 2 + 1, i, p)
        seg[n] = seg[n * 2] + seg[n * 2 + 1]

# 답 탐색 함수
def findans(s, e, n, k):
    if s == e:
        print(s)
        return
    if k <= seg[n * 2]:
        findans(s, (s + e) // 2, n * 2, k)
    else:
        findans((s + e) // 2 + 1, e, n * 2 + 1, k - seg[n * 2])

# 세그먼트트리 생성
for i in range(n):
    segmodify(1, n, 1, i + 1, sol[i])

# 명령 수행
m = int(sys.stdin.readline())
for _ in range(m):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        segmodify(1, n, 1, com[1], com[2])
    else:
        findans(1, n, 1, com[1])