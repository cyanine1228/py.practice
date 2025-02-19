# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
union = [i for i in range(n + 1)]

# 대표노드 탐색
def findp(i):
    if i == union[i]:
        return i
    return findp(union[i])

# 쿼리 수행
for M in range(m):
    q, a, b = map(int, sys.stdin.readline().split())
    if q == 0:
        union[findp(b)] = findp(a)
    else:
        if findp(a) == findp(b):
            print("YES")
        else:
            print("NO")