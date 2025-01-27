# 라이브러리 세팅 
import sys

# 테스트케이스 입력
for T in range(int(sys.stdin.readline())):

    # r e c 입력후 조건에따라 출력
    r, e, c = map(int, sys.stdin.readline().split())
    if e - r == c:
        print("does not matter")
    elif e - r < c:
        print("do not advertise")
    else:
        print("advertise")