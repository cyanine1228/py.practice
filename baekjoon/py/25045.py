# 라이브러리 세팅
import sys

# 변수 세팅 
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort(reverse = True)
b.sort()
sum = 0

# 답 출력
for i in range(min(n, m)):
    if a[i] <= b[i]:
        print(sum)
        exit(0)
    sum += a[i] - b[i]
print(sum)
exit(0)