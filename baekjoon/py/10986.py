# 라이브러리 세팅
import sys

# nC2를 구하기위한 함수
def combi(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2

# 기본 변수 세팅
n, m = map(int, sys.stdin.readline().split())

# sum은 0번째부터 k번째(k = 0, 1, 2... n)까지의 합 % m 값의 갯수
sum = [0] * m
sum[0] = 1
now = 0
lis = list(map(int, sys.stdin.readline().split()))

# sum을 구하는 과정
for i in lis:
    now = (now + i) % m
    sum[now] += 1

# 정답은 같은 나머지를 가지는 두 누적합의 조합의 수이므로
# 답을 구하여 출력
ans = 0
for i in range(m):
    ans += combi(sum[i])
print(ans)

