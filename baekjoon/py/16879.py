# 그런디수 탐색 함수
def findgrundy(x, y):
    i = 0
    while (x >= 3 * 2 ** i) | (y >= 3 * 2 ** i):
        i += 1
    if i == 0:
        grundy = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]
        return grundy[x][y]
    k = 3 * 2 ** (i - 1)
    if (k <= x) & (k <= y):
        return findgrundy(x - k, y - k)
    if x < k:
        return k + findgrundy(x, y - k)
    else:
        return k + findgrundy(x - k, y)
    
# 라이브러리 세팅 
import sys

# 모든 그런디수를 xor
ans = 0
for n in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    ans ^= findgrundy(x, y)

# 그런디 수에따라 답출력
if ans == 0:
    print("cubelover")
else:
    print("koosaga")