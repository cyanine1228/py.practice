# 라이브러리 세팅
import sys
from functools import cmp_to_key

# 임시 세팅
first = None

# ccw 함수
def ccw(a, b, c):
    k = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
    return k

# 거리 함수
def distance(a, b):
    return (a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2

# 비교 함수
def compare(a, b):
    k = ccw(first, a, b)
    if k == 0:
        return distance(first, a) - distance(first, b)
    else:
        return -k
    
# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
one = []
for i in range(n):
    x, y = map(int ,sys.stdin.readline().split())
    one.append([x, y])
dot = set()
for j in range(m):
    x1, y1 = map(int, sys.stdin.readline().split())
    for x2, y2 in one:
        dot.add((x1 + x2, y1 + y2))
dot = list(dot)
dot.sort(key = lambda x:(-x[0], -x[1]))
first = dot.pop()
dot.sort(key=cmp_to_key(compare))
dot.append(first)
stack = [first, dot[0]]
i = 1

# 컨벡스 헐 알고리즘
while i < len(dot):
    while ccw(stack[len(stack)- 2], stack[len(stack) - 1], dot[i]) <= 0:
        stack.pop()
        if len(stack) == 1:
            break
    stack.append(dot[i])
    i += 1
stack.pop()

# 답 출력
print(len(stack))
for i in stack:
    print(*i)