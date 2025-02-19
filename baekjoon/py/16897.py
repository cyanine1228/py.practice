# 그런디수 탐색 함수
def grundy(k, x, y):
    if k == 1:
        x -= 1
        y -= 1
        if (x >= 2) & (y >= 2):
            l = min(x // 2, y // 2)
            return grundy(k, x - l * 2 + 1, y - l * 2 + 1)
        if (x >= 1) & (y >= 1):
            return 1
        else:
            return (x + y) % 2
    else:
        x -= 1
        y -= 1
        k += 1
        if (x >= k * 2) & (y >= k * 2):
            K = k * 2
            l = min(x // K, y // K)
            return grundy(k, x - l * K + 1, y - l * K + 1)
        if (x >= k) & (y >= k):
            x -= k
            y -= k
            if (x >= k * 2 - 1) & (y >= k * 2 - 1):
                return 1
            else:
                return 1 - (x + y) % 2

        else:
            if (x >= k - 1) & (y >= k - 1):
                return 1
            else:
                return (x + y) % 2

# 라이브러리 세팅   
import sys

# 그런디수에따라 답출력
for T in range(int(sys.stdin.readline())):
    k, n, m = map(int, sys.stdin.readline().split())
    if grundy(k, n, m) == 0:
        print("cubelover")
    else:
        print("koosaga")

