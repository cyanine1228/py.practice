# 라이브러리 세팅
import sys
from collections import deque

# 테스트 케이스 입력 & 반복
for i in range(int(sys.stdin.readline())):

    # 기본 변수 세팅
    n, m = map(int, sys.stdin.readline().split())
    vi = {n}
    que = deque([[n, []]])

    # 목표값을 만들때까지 반복
    while True:

        # 현재 큐에서 정보 하나를 얻어온후 그 값에 따라 새 값을 큐에 저장
        k = que.popleft()

        # 얻은 정보가 m이라면 과정 출력후 반복 탈출
        if k[0] == m:
            print("".join(k[1]))
            break

        # D의 경우
        n = k[0]
        if not(n * 2 % 10000 in vi):
            vi.add(n * 2 % 10000)
            que.append([n * 2 % 10000, k[1] + ["D"]])

        # S의 경우
        if n == 0:
            if not(9999 in vi):
                vi.add(9999)
                que.append([9999, k[1] + ["S"]])
        else:
            if not(n - 1 in vi):
                vi.add(n - 1)
                que.append([n - 1, k[1] + ["S"]])

        # L, R의 경우
        d1 = n // 1000
        n %= 1000
        d2 = n // 100
        n %= 100
        d3 = n // 10
        n %= 10
        d4 = n

        # L의 경우
        n = d1 + d4 * 10 + d3 * 100 + d2 * 1000
        if not(n in vi):
            vi.add(n)
            que.append([n, k[1] + ["L"]])
        
        # R의 경우
        n = d3 + d2 * 10 + d1 * 100 + d4 * 1000
        if not(n in vi):
            vi.add(n)
            que.append([n, k[1] + ["R"]])