# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
node = [[]for i in range(n + 1)]
for i in range(n - 1):
    a, b, r = map(int, sys.stdin.readline().split())
    node[a].append([b, r])
    node[b].append([a, r])

# 거리 탐색 
for i in range(m):

    # dfs를 위한 변수 & 함수
    vi = [False] * (n + 1)
    sum = 0
    ans = 0
    def find(s, e):
        global ans
        global sum
        if s == e:
            ans = sum
            return
        for k in node[s]:
            if vi[k[0]]:
                continue
            vi[k[0]] = True
            sum += k[1]
            find(k[0], e)
            sum -= k[1]
            vi[k[0]] = False

    # dfs시행
    s, e = map(int, sys.stdin.readline().split())
    vi[s] = True
    find(s, e)

    # 답 출력
    print(ans)