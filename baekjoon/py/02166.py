# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
x = []
y = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])
sum = 0

# 신발끈
for i in range(n):
    sum += x[i] * y[i + 1]
    sum -= y[i] * x[i + 1]
sum = abs(sum)
sum /= 2

# 답 출력
print(round(sum, 1))