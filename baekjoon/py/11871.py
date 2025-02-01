# 돌개수 p일때 그런디 수:
# p = 0 : 0
# p = 홀 : p // 2 + 1
# p = 짝 : p // 2 - 1


# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
ans = -1
if p[0] == 0:
    ans = 0
elif p[0] % 2 == 1:
    ans = p[0] // 2 + 1
else:
    ans = p[0] // 2 - 1

# xor 작업
for i in range(1, n):
    k = -1
    if p[i] == 0:
        k = 0
    elif p[i] % 2 == 1:
        k = p[i] // 2 + 1
    else:
        k = p[i] // 2 - 1
    ans ^= k

# 전체 게임의 그런디 수에따라 답 출력
if ans == 0:
    print("cubelover")
else:
    print("koosaga")