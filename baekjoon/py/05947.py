# 라이브러리 세팅
import sys

# 변수 세팅
a, b, c = map(int, sys.stdin.readline().split())
res = []
for i in range(a):
    res.append(list(map(int, sys.stdin.readline().split())))

# 조건을 만족하는 대대답만 유지
for _ in range(c):
    res2 = []
    q, score = map(int, sys.stdin.readline().split())
    for K in res:
        if K[q - 1] == score:
            res2.append(list(K))
    res = list(res2)

# 대답의 개수 출력
print(len(res))