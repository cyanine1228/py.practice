# 라이브러리 세팅
import sys
from collections import deque

# 기본 변수 세팅
n, m = map(int, sys.stdin.readline().split())
node = [[[], []] for i in range(n + 1)]
for M in range(m):
    order = list(map(int, sys.stdin.readline().split()))
    for i in range(1, order[0]):
        node[order[i]][1].append(order[i + 1])
        node[order[i + 1]][0].append(order[i])
ans = []
que = deque()
for i in range(1, n + 1):
    if len(node[i][0]) == 0:
        que.append(i)

# 큐에 남은 값이 없을때까지 반복(위상정렬)
while len(que) != 0:

    # 큐에서 수 하나를 빼어 다음에 연결되는 수의 간선 제거, 조건을 만족한다면 큐에 추가
    k = que.popleft()
    ans.append(k)
    for i in node[k][1]:
        node[i][0].remove(k)
        if len(node[i][0]) == 0:
            que.append(i)
    node[k][1] = []

# 만약 모든 순서가 정렬될 수 있다면 답출력, 아니라면 0 출력
if len(ans) == n:
    for i in ans:
        print(i)
else:
    print(0)