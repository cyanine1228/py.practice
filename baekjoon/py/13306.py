# 라이브러리 세팅
import sys

# 재귀 깊이 세팅
sys.setrecursionlimit(300000)

# 변수 세팅
n, q = map(int, sys.stdin.readline().split())
p = [None, None]
for i in range(n - 1):
    p.append(int(sys.stdin.readline()))
query = []
for i in range(n - 1 + q):
    query.append(list(map(int, sys.stdin.readline().split())))
tree = [i for i in range(n + 1)]

# 부모 노드를 찾는 함수
def findp(k):
    if k == tree[k]:
        return k
    tree[k] = findp(tree[k])
    return tree[k]

# 쿼리 수행(역순으로)
ans = []
for i in range(len(query) - 1, -1, -1):
    j = query[i]
    if j[0] == 0:
        tree[findp(j[1])] = p[j[1]]
    else:
        if findp(j[1]) == findp(j[2]):
            ans.append("YES")
        else:
            ans.append("NO")

# 답 출력
for i in range(len(ans) - 1, -1, -1):
    print(ans[i])