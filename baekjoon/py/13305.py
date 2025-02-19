# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
i = 0
mincost = 100000000000000
ans = 0

# 모든 길을 탐색하며 진행
while i != n - 1:

    # i번째 주유소에서 i + 1번째 주유소까지 가기위한 기름값의 최소값(역대 기름값의 최소값) 갱신
    mincost = min(mincost, cost[i])

    # 거리 * 기름값만큼 답에 추가
    ans += dis[i] * mincost

    # i에 1추가(다음 주유소로)
    i += 1

# 답 출력
print(ans)