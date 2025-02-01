# 라이브러리 세팅
import sys

# n, k 세팅
n, k = map(int, sys.stdin.readline().split())
k %= 2

# k의 값에 따라 사용할 두가지 그런디수 함수
def grundy1(n): # k 짝
    if n <= 2:
        return n
    return 1 - n % 2

def grundy2(n): # k 홀
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 4 == 2:
        return 0
    if n % 4 == 3:
        return 1
    if n % 4 == 0:
        return 2
    if n % 4 == 1:
        return 0
    
# 각 값의 그런디 수에따라 xor 연산
ans = 0
p = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    if k % 2 == 0:
        ans ^= grundy1(p[i])
    else:
        ans ^= grundy2(p[i])

# 최종 게임 그런디수가 0인지에 따라 승자 출력
if ans == 0:
    print("Nicky")
else:
    print("Kevin")
