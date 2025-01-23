import sys
from collections import deque
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
while len(que) != 0:
    k = que.popleft()
    ans.append(k)
    for i in node[k][1]:
        node[i][0].remove(k)
        if len(node[i][0]) == 0:
            que.append(i)
    node[k][1] = []
if len(ans) == n:
    for i in ans:
        print(i)
else:
    print(0)