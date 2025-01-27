# 라이브러리 세팅
import sys

# 재귀 세팅
sys.setrecursionlimit(10**4)

# 승리여부 결정 함수
def winif(n):
    if win.get(n, "X") != "X":
        return win[n]
    i = 0
    while k ** i <= n:
        i += 1
    i -= 1
    while i >= 0:
        l = n - k ** i
        if winif(l) == 0:
            win[n] = k ** i
            return k ** i
        i -= 1
    win[n] = 0
    return 0

# 테스트 케이스 입력
for T in range(int(sys.stdin.readline())):

    # 변수 선언
    s, k = map(int, sys.stdin.readline().split())

    # 특이케이스(k = 1) 분리
    if k == 1:
        if s % 2 == 0:
            print(0)
        else:
            print(1)
        continue

    # 답 출력
    win = {0 : 0}
    ans = winif(s)
    if ans == 0:
        print(0)
    else:
        i = 0
        while True:
            if winif(s - k ** i) == 0:
                print(k ** i)
                break
            i += 1
