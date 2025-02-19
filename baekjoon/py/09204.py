# 라이브러리 세팅
import sys

# 테스트 케이스 수 입력
for T in range(int(sys.stdin.readline())):

    # 변수 세팅
    a, b, c, d = sys.stdin.readline().split()
    a = ord(a) - 64
    b = int(b)
    c = ord(c) - 64
    d = int(d)

    # 불가능한 경우 처리
    if ((a + b) % 2) != ((c + d) % 2):
        print("Impossible")
        continue

    # 이동0번인 경우 처리
    if (a == c) & (b == d):
        print("0 {} {}".format(chr(a + 64), b))
        continue

    # 이동 1번인 경우 처리
    if abs(a - c) == abs(b - d):
        print("1 {} {} {} {}".format(chr(a + 64), b, chr(c + 64), d))
        continue

    # 이동 2번인 경우 처리
    board = [[0] * 9 for i in range(9)]
    for i in range(9):
        if (a + i < 9) & (b + i < 9):
            board[a + i][b + i] = 1
        if (a + i < 9) & (b - i >= 1):
            board[a + i][b - i] = 1
        if (a - i >= 1) & (b + i < 9):
            board[a - i][b + i] = 1
        if (a - i >= 1) & (b - i >= 1):
            board[a - i][b - i] = 1
    ans = 0
    for i in range(9):
        if (c + i < 9) & (d + i < 9):
            if board[c + i][d + i] == 1:
                ans = [c + i, d + i]
                break
        if (c + i < 9) & (d - i >= 1):
            if board[c + i][d - i] == 1:
                ans = [c + i, d - i]
                break
        if (c - i >= 1) & (d + i < 9):
            if board[c - i][d + i] == 1:
                ans = [c - i, d + i]
                break
        if (c - i >= 1) & (d - i >= 1):
            if board[c - i][d - i] == 1:
                ans = [c - i, d - i]
                break
    print("2", chr(a + 64), b, chr(ans[0] + 64), ans[1], chr(c + 64), d)