# 라이브러리 세팅
import sys

# 기본 변수 세팅
dp = [0] * 501
node = [-100] * 501
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    node[a] = b

# 가장 긴 증가하는 부분수열의 길이를 탐색(dp에 저장된값중 하나)
for i in range(1, 501):
    if node[i] == -100:
        continue
    if dp[node[i]] < 1 + max(dp[:node[i]]):
       dp[node[i]] = 1 + max(dp[:node[i]])
    
# 전체 전깃줄 수에서 가장 긴 증가하는 부분수열의 길이를 뺀것이 답이므로 출력
print(n - max(dp))

