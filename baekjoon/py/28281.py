# 라이브러리 세팅
import sys       

# n, x, 가격표 입력
n, x = map(int, sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))

# 최소비용 탐색 알고리즘
ans = 100000000000000000000                 # 최소비용 기본값 세팅
for i in range(1, n):                       # 리스트를 탐색하며 최소비용 갱신
    if (lis[i] + lis[i - 1]) * x < ans:
        ans = (lis[i] + lis[i - 1]) * x

# 답 출력
print(ans)                  