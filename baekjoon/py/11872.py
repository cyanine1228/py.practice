# 라이브러리 세팅
import sys

# 그런디 수 찾기 함수
def findgrundy(n):
    if n == 0:
        return 0
    if n % 4 == 0:
        return n - 1
    if n %  4 == 3:
        return n + 1
    return n

# 답 탐색
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
ans = findgrundy(p[0])
for i in range(1, n):
    ans ^= findgrundy(p[i])
if ans == 0:
    print("cubelover")
else:
    print("koosaga")