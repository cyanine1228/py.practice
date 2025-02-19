# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
tree = [i for i in range(n + 1)]
node = []
for i in range(m):
    node.append(list(map(int, sys.stdin.readline().split())))
node.sort(key = lambda x:x[2])

# 루트 탐색 함수
def findp(k):
    if k == tree[k]:
        return k
    tree[k] = findp(tree[k])
    return tree[k]

# 크루스칼 알고리즘
i = 1
j = 0
ans = 0
while i < n:
    a, b, c = node[j]
    j += 1
    if findp(a) == findp(b):
        continue
    tree[findp(a)] = findp(b)
    ans += c
    i += 1

# 답 출력 : 최소 스패닝 트리에서 가장 가중치가 높은길을 끊어 두 마을을 분할
print(ans - c)