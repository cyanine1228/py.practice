# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
dic = {}

# 딕셔너리 생성
for N in range(n):
    l = list(sys.stdin.readline().split())
    dic[l[0]] = l[1]

# 딕셔너리를 통한 출력
for M in range(m):
    print(dic[sys.stdin.readline().strip()])