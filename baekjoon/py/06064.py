# 라이브러리 세팅
import sys
import math

# 테스트 케이스 수 입력
for T in range(int(sys.stdin.readline())):

    # 변수 세팅
    m, n, x, y = map(int, sys.stdin.readline().split())
    i = 0

    # 가능한 경우의수 순회
    while m * i + x - y <= math.lcm(m, n):

        # 값 탐색에 성공했다면 출력후 탈출
        if (m * i + x - y) % n == 0:
            print(m * i + x)
            break
        
        # 카운트에 1 추가
        i += 1

    # 가능한 경우의수가 없다면 -1 출력
    else:
        print(-1)