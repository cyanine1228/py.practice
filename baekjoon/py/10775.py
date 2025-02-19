# 라이브러리 세팅
import sys

# 변수 세팅
g = int(sys.stdin.readline())
vi = [i for i in range(g + 1)]
p = int(sys.stdin.readline())
ans = 0

# 루트 탐색 함수
def findp(k):
    if k == vi[k]:
        return k
    vi[k] = findp(vi[k])
    return vi[k]

# 그리디 알고리즘
for i in range(p):
    k = int(sys.stdin.readline())
    if findp(k) == 0:
        for j in range(p - i - 1):
            sys.stdin.readline()
        print(ans)
        exit(0)
    ans += 1
    vi[findp(k)] = findp(findp(k) - 1)
print(ans)