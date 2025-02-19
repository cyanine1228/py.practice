# 일반 님게임으로 가정, k개의 돌더미에 1, 2, 3, 4.... k개의 돌이있을때 그런디수 반환
def one_z_grundy(k):
    if k == 0:
        return 0
    if k % 4 == 1:
        return 1
    if k % 4 == 2:
        return k + 1
    if k % 4 == 3:
        return 0
    return k

# 일반 님게임으로 가정, 각 돌더미에 x, x + 1, x + 2....x + m - 1개의 돌이있을때 그런디수 반환
def grundy(x, m):
    return one_z_grundy(x + m - 1) ^ one_z_grundy(x - 1)

# 라이브러리 세팅
import sys

# 그런디수 탐색
ans = 0
n = int(sys.stdin.readline())
for i in range(n):
    x, m = map(int, sys.stdin.readline().split())
    ans ^= grundy(x, m)

# 그런디 수에따라 답 출력 
if ans == 0:
    print("cubelover")
else:
    print("koosaga")