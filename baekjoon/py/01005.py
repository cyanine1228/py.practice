# 라이브러리 세팅
import sys
from collections import deque

# 테스트 케이스 입력
for T in range(int(sys.stdin.readline())):

    # 기본 변수 세팅
    n, k = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    node = [[[], []]for i in range(n + 1)]
    node2 = [[[], []]for i in range(n + 1)]
    que = deque()
    order = []
    ans = [-1] * (n + 1) 

    # 위상정렬을 위한 간선 세팅
    for i in range(k):
        s, t = map(int,  sys.stdin.readline().split())
        node[s][1].append(t)
        node[t][0].append(s)
        node2[s][1].append(t)
        node2[t][0].append(s)

    goal = int(sys.stdin.readline())

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

    # 위상정렬된 순서에따라 해당 건물 건설시 필요한 시간을 ans에 저장후 목표 건물이라면 출력
    for i in order:

        # 만약 먼저 건설해야될 건물이 없다면 필요 시간 == 기본 소요시간
        if len(node2[i][0]) == 0:
            ans[i] = time[i]
        
        # 먼저 건설해야될 건물이 있다면 현재 건물 필요시간 == 먼저 건설해야될 건물들의 필요시간 최대값 + 기본소요시간
        else:
            ma = 0
            for j in node2[i][0]:
                if ma < ans[j]:
                    ma = ans[j]
            ans[i] = ma + time[i]

        # 만약 목표건물이라면 값 출력
        if i == goal:
            print(ans[i])
            break