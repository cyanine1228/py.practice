# 라이브러리 세팅
import sys

while True:

    # n, m 입력
    n, m = map(int, sys.stdin.readline().split())

    # 0 0 이면 탈출
    if n == m == 0:
        break

    # 변수 세팅
    lis = []
    for i in range(n):
        lis.append(int(sys.stdin.readline()))
    sum = 0

    # 이분 탐색으로 답 탐색
    for _ in range(m):
        i = 0
        j = n - 1
        k = int(sys.stdin.readline())
        while i < j:
            if lis[(i + j) // 2] == k:
                sum += 1
                break
            elif lis[(i + j) // 2] > k:
                j = (i + j // 2) - 1
            else:
                i = (i + j // 2) + 1
            if (i == j):
                if (lis[i] == k):
                    sum += 1
                    break
                
    # 답 출력
    print(sum)