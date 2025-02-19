# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
board = []
num = set()
for i in range(0, 100000):
    num.add(i ** 2)
for _ in range(n):
    board.append(list(map(int, list(sys.stdin.readline().strip()))))
max = -1

# 탐색

# i, j번째 칸을 시작으로 하는 정수
for i in range(n):
    for j in range(m):

        # 한번에 세로로 I칸씩, 가로로 J칸씩 이동
        for I in range(0, n + 1):
            for J in range(0, m + 1):

                # 만약 이동불가능한 상태라면 패스
                if (I == 0) & (J == 0):
                    continue

                # 오른쪽 아래로 내려가는 경우
                p, q = i, j
                a = ""
                while (p < n) & (q < m):
                    a = a + str(board[p][q])
                    if (int(a) in num) & (int(a) > max):
                        max = int(a)
                    p += I
                    q += J

                # 왼쪽 아래로 내려가는 경우
                p, q = i, j
                a = ""
                while (p < n) & (q >= 0):
                    a = a + str(board[p][q])
                    if (int(a) in num) & (int(a) > max):
                        max = int(a)
                    p += I
                    q -= J
                p, q = i, j
                a = ""

                # 오른쪽 위로 올라가는 경우
                while (p >= 0) & (q < m):
                    a = a + str(board[p][q])
                    if (int(a) in num) & (int(a) > max):
                        max = int(a)
                    p -= I
                    q += J
                p, q = i, j
                a = ""

                # 왼쪽 위로 올라가는 경우
                while (p >= 0) & (q >= 0):
                    a = a + str(board[p][q])
                    if (int(a) in num) & (int(a) > max):
                        max = int(a)
                    p -= I
                    q -= J

# 최대값 출력
print(max)