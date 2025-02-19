# 라이브러리 세팅
import sys

# 변수 세팅
n, m, b = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    board += list(map(int, sys.stdin.readline().split()))
board.sort(reverse=True)
sum = 0
for i in board:
    sum += i
sum += b
ans = 10000000000000
ansheight = -1

# 0 ~ 256 사이 높이를 순회하며, 그 높이로 만들 때의 시간에 따라 답 갱신
for i in range(257):

    # 변수 세팅
    res = 0

    # 만약 높이i로 만들 수 없다면 패스
    if i * n * m > sum:
        continue

    # 보드 순회
    for j in board:

        # 목표높이와 현재높이의 높이차
        k = j - i

        # 만약 높이차가 양수라면(깎아야 한다면) 깎는 양 * 2만큼 res에 추가
        if k > 0:
            res += k * 2

        # 높이차가 음수라면(설치해야 한다면) 이미 완성가능한것은 위에서 증명되었으므로 설치량만큼 res에 추가
        else:
            res += -k

    # 만약 이번 결과가 답ans보다 작다면 갱신 
    if ans >= res:
        ans = res
        ansheight = i

# 답 출력
print(ans, ansheight)