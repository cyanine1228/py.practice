# 라이브러리 세팅
import sys

# 기본 변수 세팅
n, k = map(int, sys.stdin.readline().split())
degree = list(map(int, sys.stdin.readline().split()))
sum = [0]

# sum에 누적합을 저장
for i in range(0, n):
    sum.append(sum[i] + degree[i])

# 누적합을 이용하여 온도의 최댓값을 탐색
ma = -10000000000000
for i in range(k ,n + 1):
    if sum[i] - sum[i - k] > ma:
        ma = sum[i] - sum[i - k]

# 최댓값 출력
print(ma)