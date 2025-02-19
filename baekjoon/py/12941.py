# 라이브러리 세팅
import sys

# 변수 세팅
n, k = map(int, sys.stdin.readline().split())
k %= 2

# 그런디수 탐색 함수
def grundy(p):
    if k == 0:
        if p <= 2:
            return p
        else:
            return 1 - p % 2
    else:
        if p <= 6:
            l = [0, 1, 0, 1, 2, 0, 2]
            return l[p]
        else:
            if p % 2 == 1:
                return 0
            else:
                if grundy(p // 2) == 1:
                    return 2
                else:
                    return 1
                
# ans에 각각의 그런디수를 xor
a = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in a:
    ans ^= grundy(i)

# ans의 값에따라 답 탐색
if ans == 0:
    print("Nicky")
else:
    print("Kevin")