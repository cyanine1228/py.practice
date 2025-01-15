# 라이브러리 세팅
import math

# 기본 세팅
n = int(input())
sum = 1

# 계산
for i in range(1, n + 1):
    sum *= i

# 출력
print(sum)