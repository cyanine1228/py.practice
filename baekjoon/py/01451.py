import sys                                                                  # 빠른 입출력을 위한 sys 라이브러리
n, m = map(int, sys.stdin.readline().split())                               # n, m 입력
board = []                                                                  # 보드 초기화
for i in range(n):                                                          # n회 반복해서 보드 입력
    board.append(list(map(int, list(sys.stdin.readline().strip()))))        # 보드 입력
ma = 0                                                                      # 최대치는 0


# 1   1 1
# 1
# 1   1 1 
# 1   1 1

# 위와 같은 형식으로 3등분 되는 경우

for i in range(1, n):                                                       # 세 직사각형의 모든 모서리가 겹치는 지점의 y좌표                                           #
    for j in range(1, m):                                                   # 세 직사각형의 모든 모서리가 겹치는 지점의 x좌표
        sum1 = 0                                                            # 만들어진 네 직사각형중 왼쪽위의 직사각형의 합
        for p in range(0, i):
            for q in range(0, j):
                sum1 += board[p][q]     
        sum2 = 0                                                            # 만들어진 네 직사각형중 오른쪽위의 직사각형의 합
        for p in range(i, n):
            for q in range(0, j):
                sum2 += board[p][q]
        sum3 = 0                                                            # 만들어진 네 직사각형중 왼쪽아래의 직사각형의 합
        for p in range(0, i):
            for q in range(j, m):
                sum3 += board[p][q]
        sum4 = 0                                                            # 만들어진 네 직사각형중 오른쪽아래의 직사각형의 합
        for p in range(i, n):
            for q in range(j, m):
                sum4 += board[p][q]
        summa = max((sum1 + sum2) * sum3 * sum4, (sum1 + sum3) * sum2 * sum4,(sum2 + sum4) * sum1 * sum3,(sum3 + sum4) * sum1 * sum2) # 네 사각형중 두 사각형을 합친후 계산한 값중 최소값값
        if summa > ma:                                                      # 이 값이 최소값보다 작다면
            ma = summa                                                      # 최소값 갱신


# 1 1 1 1 1
# 
# 1 1 1 1 1
#
# 1 1 1 1 1

# 위와 같은 방식으로 3등분 되는 경우(원리자체는 같으므로 주석 생략)

for i in range(1, n - 1):
    for j in range(i + 1, n):
        sum1 = 0
        for p in range(0, i):
            for q in range(0, m):
                sum1 += board[p][q]
        sum2 = 0
        for p in range(i, j):
            for q in range(0, m):
                sum2 += board[p][q]
        sum3 = 0
        for p in range(j, n):
            for q in range(0, m):
                sum3 += board[p][q]
        summa = sum1 * sum2 * sum3
        if summa > ma:
            ma = summa


# 1   1   1
# 1   1   1
# 1   1   1
# 1   1   1
# 1   1   1

# 위와 같은 방식으로 3등분 되는 경우

for i in range(1, m - 1):
    for j in range(i + 1, m):
        sum1 = 0
        for p in range(0, n):
            for q in range(0, i):
                sum1 += board[p][q]
        sum2 = 0
        for p in range(0, n):
            for q in range(i, j):
                sum2 += board[p][q]
        sum3 = 0
        for p in range(0, n):
            for q in range(j, m):
                sum3 += board[p][q]
        summa = sum1 * sum2 * sum3
        if summa > ma:
            ma = summa
print(ma)                                                                   # 최소값 출력