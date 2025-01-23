# 라이브러리 세팅
import sys

# 기본 변수 세팅
n = int(sys.stdin.readline())                                   # 사각형 수
group = []                                                      # 사각형 좌표를 저장할 배열
crossO = False                                                  # 원점을 지나는지 여부를 저장할 변수
node = [[]for i in range(n)]                                    # 서로 겹치는 사각형들을 하나로 묶기 위해 dfs를 사용할 그래프
vi = [False] * n                                                # dfs 사용시 방문한 점을 예외처리하기 위한 배열
stack = []                                                      # dfs 사용시 사용할 스택택

# 사각형 입력 & 그룹 묶기
for i in range(n):

    # 좌표 입력
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    # 원점을 지나면 crossO를 True로 변경
    if ((x1 == 0) | (x2 == 0)) & (y1 * y2 <= 0):
        crossO = True
    if ((y1 == 0) | (y2 == 0)) & (x1 * x2 <= 0):
        crossO = True


    # 앞에 입력했었던 사각형을 하나씩 불러오며 판별
    for j in range(i):  

        # 앞에 입력했었던 사각형의 정보 불러오기
        x3, y3, x4, y4 = group[j]

        # 현 사각형이 전 사각형보다 왼쪽에 있다면 겹치지 않으므로 넘어감
        if x2 < x3:
            continue

        # 현 사각형이 전 사각형보다 오른쪽에 있다면 겹치지 않으므로 넘어감
        if x1 > x4:
            continue

        # 현 사각형이 전 사각형보다 아래쪽에 있다면 겹치지 않으므로 넘어감
        if y2 < y3:
            continue

        # 현 사각형이 전 사각형보다 위쪽에 있다면 겹치지 않으므로 넘어감
        if y1 > y4:
            continue

        # 현 사각형이 전 사각형 안에 있다면 겹치지 않으므로 넘어감
        if (x3 < x1 < x2 < x4) & (y3 < y1 < y2 < y4):
            continue

        # 현 사각형이 전 사각형을 포함한다면 넘어감
        if (x1 < x3 < x4 < x2) & (y1 < y3 < y4 < y2):
            continue

        # 겹치는 사각형이 있다면 node에 서로 간선을 추가가
        node[i].append(j)
        node[j].append(i)

    # 이번 사각형 정보 저장
    group.append([x1, y1, x2, y2])

# dfs를 통해서 겹치지 않는 사각형 수 합 구하기
sum = 0
for i in range(n):
    if vi[i]:
        continue
    sum += 1
    stack.append(i)
    vi[i] = True
    while len(stack) != 0:
        k = stack.pop()
        for j in range(len(node[k])):
            if vi[node[k][j]]:
                continue
            stack.append(node[k][j])
            vi[node[k][j]] = True 

# 원점을 지나면 -1
if crossO:
    sum -= 1

# 답 출력
print(sum)