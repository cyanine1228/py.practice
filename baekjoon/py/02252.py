# 라이브러리 세팅
import sys
from collections import deque

# 기본 변수 세팅
n, m = map(int, sys.stdin.readline().split())
node = [[[], []]for i in range(n + 1)]
que = deque()
order = []

# 위상정렬을 위한 간선 세팅
for i in range(m):
    s, t = map(int,  sys.stdin.readline().split())
    node[s][1].append(t)
    node[t][0].append(s)

# 위상정렬 시작점을 찾기위하여 진입차수가 0인 번호를 찾아 큐에 삽입
for i in range(1, n + 1):
    if len(node[i][0]) == 0:
        que.append(i)

# 위상정렬
while len(que) != 0:
    k = que.popleft()
    order.append(k)
    for i in range(len(node[k][1])):
        node[node[k][1][i]][0].remove(k)
        if len(node[node[k][1][i]][0]) == 0:
            que.append(node[k][1][i])
    node[k][1] = []

# 답 출력
print(*order)