# 라이브러리 세팅
import sys

# 변수 세팅
v, e = map(int, sys.stdin.readline().split())
tree = [i for i in range(v + 1)]
node = []
for i in range(e):
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
while i < v:
    a, b, c = node[j]
    j += 1
    if findp(a) == findp(b):
        continue
    tree[findp(a)] = findp(b)
    ans += c
    i += 1

# 답 출력
print(ans)