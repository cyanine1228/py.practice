# 라이브러리 세팅
import sys
from collections import deque

# 기본 변수 세팅
f, s, g, u, d = map(int, sys.stdin.readline().split())
vi = [True] + [False] * f
vi[s] = True
sum = 0
que = deque([s])

# 실제 실행(bfs 이용)
while len(que) != 0:

    # 이번큐에 답이 포함되어 있다면 sum 출력후 탈출
    if g in que:
        print(sum)
        exit(0)

    # 이번큐에 저장된 모든 층을 빼내고 U D값에 따라 큐에 다음 층 저장
    for i in range(len(que)):
        k = que.popleft()
        if (k + u <= f):
            if not(vi[k + u]):
                vi[k + u] = True
                que.append(k + u)
        if (k - d >= 1):
            if not(vi[k - d]):
                vi[k - d] = True
                que.append(k - d)

    # 1회 이동하였으므로 sum에 1 추가
    sum += 1

# 만약 큐 길이가 0이라면(더이상 가능한 경우의수가 없다면) 예외 문구 출력
else:
    print("use the stairs")