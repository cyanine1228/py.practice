# 라이브러리 세팅
import sys

# 기본 변수 입력 & 세팅
n, i = map(int, sys.stdin.readline().split())
handle = []

# 핸들 입력
for j in range(n):
    handle.append(sys.stdin.readline().strip())

# 핸들 정렬
handle.sort()

# 출력
print(handle[i - 1])