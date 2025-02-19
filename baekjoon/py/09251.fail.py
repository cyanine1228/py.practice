# 변수 세팅
a = list(input())
b = list(input())
x = len(a)
y = len(b)
board = [[0] * y for i in range(x)]
ma = 0

# LCS 탐색
for i in range(x):
    for j in range(y):
        if a[i] == b[j]:
            k = 0
            for p in range(i):
                for q in range(j):
                    k = max(k, board[p][q])
            board[i][j] = k + 1
            ma = max(ma, k + 1)

# 최대값 출력
print(ma)