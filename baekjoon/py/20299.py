# 라이브러리 세팅
import sys

# 기본 변수 입력&세팅
n, k, l = map(int, sys.stdin.readline().split())
ans = []
sum = 0

# 각 입력마다 체크하며 ans와 sum 업데이트
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    if (a < l) | (b < l) | (c < l):                     # l에 대한 조건 확인
        continue
    if a + b + c < k:                                   # k에 대한 조건 확인
        continue
    sum += 1
    ans.extend([a, b, c])

# 답 출력
print(sum)
print(*ans)