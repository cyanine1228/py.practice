# 라이브러리 세팅
import sys

# 재귀 깊이 세팅
sys.setrecursionlimit(10 ** 5)

# 변수 세팅
n = int(sys.stdin.readline())
inorder = [-1] + list(map(int, sys.stdin.readline().split())) + [-1]
inordernum = [-1] * (n + 1)  + [-1]
for i in range(1, n + 1):
    inordernum[inorder[i]] = i
postorder = list(map(int, sys.stdin.readline().split()))
tree = {}

# 트리 생성
for i in postorder:
    info = [None, None, None]
    index = inordernum[i]

    # 왼쪽 자식이 존재한다면 왼쪽 자식을 info[0]에 저장, 왼쪽자식의 부모를 저장
    if (inorder[index - 1] != -1) & (tree.get(inorder[index - 1], "F") != "F"):
        lindex = inorder[index - 1]
        while tree[lindex][2] != None:
            lindex = tree[lindex][2]
        tree[lindex][2] = i
        info[0] = lindex

    # 오른쪽 자식이 존재한다면 오른쪽 자식을 info[1]에 저장, 오른쪽 자식의 부모를 저장
    if (inorder[index + 1] != -1) & (tree.get(inorder[index + 1], "F") != "F"):
        rindex = inorder[index + 1]
        while tree[rindex][2] != None:
            rindex = tree[rindex][2]
        tree[rindex][2] = i
        info[1] = rindex

    # 정점 추가
    tree[i] = list(info)

# 프리오더 출력함수
def preorder(n):
    print(n, end = " ")
    if tree[n][0] != None:
        preorder(tree[n][0])
    if tree[n][1] != None:
        preorder(tree[n][1])

# 실행
preorder(postorder[len(postorder) - 1])