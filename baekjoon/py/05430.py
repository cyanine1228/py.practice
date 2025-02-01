# 라이브러리 세팅
import sys
from collections import deque
# 테스트 케이스 입력
for T in range(int(sys.stdin.readline())):

    # 명령 입력
    com = list(sys.stdin.readline().strip())

    # 배열 길이 입력
    n = int(sys.stdin.readline())

    # 배열 입력
    x = sys.stdin.readline().strip()
    x = x[1:len(x) - 1]
    x = deque(x.split(","))
    if x[0] == "":
        x = []
    rev = False

    # 명령 수행
    for i in com:
        if i == "R":
            if rev:
                rev = False
            else:
                rev = True
        else:
            if len(x) == 0:
                print("error")
                break
            if rev:
                x.pop()
            else:
                x.popleft()
    else:
        if rev:
            x.reverse()
        print("[", end = "")
        l = len(x)
        for i in range(l):
            if i == l - 1:
                print(x.popleft(), end = "")
            else:
                print(x.popleft(), end = ",")
        print("]")