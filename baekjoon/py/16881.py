# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
ans = 0

# 각 행에 대한 그런디수를 ans에 xor
for i in range(n):
    p = list(map(int, sys.stdin.readline().split()))
    k = 100000000
    for i in range(m - 1, -1, -1):
        if k <= p[i] - 1:
            k = p[i]
        else:
            k = p[i] - 1
    ans ^= k

# xor값에따라 답 출력
if ans == 0:
    print("cubelover")
else:
    print("koosaga")