# 변수 세팅
n = int(input())
parent = list(map(int, input().split()))
node = [[-2, []]for i in range(n)]
root = -1
for i in range(n):
    node[i][0] = parent[i]
    if parent[i] == -1:
        root = i
    else:
        node[parent[i]][1].append(i)

# 지울 노드 입력 
k = int(input())

# 예외 처리(삭제노드가 루트노드인경우)
if k == root:
    print(0)
    exit(0)

# 노드 삭제
node[node[k][0]][1].remove(k)
stack = [root]

# dfs를 이용하여 리프노드 수 탐색
ans = 0
while len(stack) != 0:
    k = stack.pop()
    if len(node[k][1]) == 0:
        ans += 1
        continue
    for i in node[k][1]:
        stack.append(i)

# 답 출력
print(ans)