# 라이브러리 세팅
import sys

# 기본 변수 세팅
n = int(sys.stdin.readline())
node = []
for i in range(n):
    node.append(list(map(int, sys.stdin.readline().split())))
check = (1 << n) - 1
sum = 0
mi = 100000000000000000

stack = [0]
while len(stack) != 0:
    k = stack.pop()
    check &= (~(1 << k))
    if check == 0:
        if node[i][0] == 0:
            continue
        else:
            mi = min(mi, sum + node[i][0])
            continue
    
# 재귀함수를 이용하여 모든 경우의 수 탐색
def dfs(i):

    # 전역변수 선언
    global sum
    global mi
    global check

    # 만약 모든 도시를 방문했다면
    if check == 0:

        # 시작지점으로 돌아갈 수 없다면 리턴
        if node[i][0] == 0:
            return
        
        # 시작지점으로 돌아갈 수 있다면 돌아가는 비용을 포함하여 최소값 갱신
        else:
            mi = min(mi, sum + node[i][0])
            return
        
    # 아직 모든도시를 방문하지 않았다면 다음도시를 방문
    for j in range(n):

        # 방문할 수 없는 도시라면 다른 경우의수 탐색
        if node[i][j] == 0:
            continue

        # 이미 방문한 도시라면 다른 경우의수 탐색
        if not((check & (1 << j)) != 0):
            continue

        # 방문처리후 함수 재호출
        check &= (~(1 << j))
        sum += node[i][j]
        dfs(j)
        sum -= node[i][j]
        check |= (1 << j)

# 함수실행후 최소값 출력
check &= (~(1 << 0))
dfs(0)
print(mi)