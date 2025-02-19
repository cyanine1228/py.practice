# 라이브러리 세팅
import sys

# 변수 세팅
c, p = map(int, sys.stdin.readline().split())
board = list(map(int, sys.stdin.readline().split())) + [100000000000] * 4

# 각 미노마다, 그리고 각 회전마다 각 칸들의 높이차이를 저장한 함수
mino_table = [[[0],  [0, 0, 0, 0]],
              [[0, 0]],
              [[0, 0, 1], [0, -1]],
              [[0, -1, -1], [0, 1]],
              [[0, 0, 0], [0, -1, 0], [0, 1], [0, -1]],
              [[0, 0, 0], [0, 0], [0, -2], [0, 1, 1]],
              [[0, 0, 0], [0, 0], [0, 2], [0, 0, -1]]]

# board의 k부터 높이의 변화가 a와 동일한 경우 True(블록 설치가능), 아니면 False 반환
def compare(a, k):
    first = board[k]
    for i in range(len(a)):
        if first + a[i] != board[k + i]:
            return False
    return True

# 모든 테이블에대해 compare함수를 실행하여 답을 탐색
ans = 0
for i in mino_table[p - 1]:
    for j in range(c):  
        if compare(i, j):
            ans += 1

# 답 출력
print(ans)