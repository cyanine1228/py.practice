# 각 행마다의 그런디 수는 그 행에서 모든 열의 값의 합

# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
ans = 0

# 모든 행에 대해 xor
for i in range(n):
    sum = 0
    p = list(map(int, sys.stdin.readline().split()))
    for j in p:
        sum += j
    ans ^= sum

# 전체 게임의 그런디 수에따라 승자 출력
if ans == 0:
    print("ainta")
else:
    print("august14")