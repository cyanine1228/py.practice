# 라이브러리 세팅
import math

# 입력
n = int(input())
m = list(map(int, input().split()))

# 최대공약수 저장
if n == 2:
    k = math.gcd(m[0], m[1])
else:
    k = math.gcd(m[0], m[1], m[2])

# 최대공약수의 약수 출력
i = 1
while i <= k:
    if k % i == 0:
        print(i)
    i += 1