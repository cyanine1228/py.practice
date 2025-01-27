# 라이브러리 세팅
import sys

# 상금 최대값 선언
sum = 0

for T in range(int(sys.stdin.readline())):

    # 입력후 조건에따라 최대값 갱신
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c:
        sum = max(sum, a * 1000 + 10000)
    elif (a == b != c) | (a == c != b):
        sum = max(sum, a * 100 + 1000)
    elif b == c != a:
        sum = max(sum, b * 100 + 1000) 
    else:
        sum = max(sum, max(a, b, c) * 100)

# 출력
print(sum)

