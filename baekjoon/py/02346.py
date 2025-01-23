# 라이브러리 세팅
import sys
from collections import deque

# 기본 변수 세팅
n = int(sys.stdin.readline())
command = list(map(int, sys.stdin.readline().split()))
number = [i for i in range(1, n + 1)]
que = deque(zip(command, number))

# 실제 실행
while True:

    # 덱에서 한개를 뽑은후 번호 출력
    k = que.popleft()
    print(k[1], end = " ")

    # 더이상 덱에 남은것이 없다면 종료
    if len(que) == 0:
        break

    # 뽑은 지시대로 덱을 이동
    if k[0] > 0:
        for j in range(k[0] - 1):
            que.append(que.popleft())
    else:
        for j in range(-k[0]):
            que.appendleft(que.pop())