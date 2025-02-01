# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
s = int(sys.stdin.readline())

# 비교, 정답 출력
for i in range(1, n):
    if s < int(sys.stdin.readline()):
        print("N")
        exit(0)
else:
    print("S")