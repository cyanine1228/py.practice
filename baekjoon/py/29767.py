# 라이브러리 세팅
import sys

# 변수 세팅
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 누적합 세팅후 역정렬
sum = [0]
for i in a:
    sum.append(sum[len(sum) - 1] + i)
sum.pop(0)
sum.sort(reverse=True)

# 답 출력
ans = 0
for i in range(k):
    ans += sum[i]
print(ans)