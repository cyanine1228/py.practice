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
n = int(sys.stdin.readline())
dot = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dot.append([x, y, i])
ans = [0] * n

# 컨벡스헐 알고리즘으로 층 마다 꼭짓점 저장
floor = 1
while True:
    if len(dot) <= 2:
        break
    dot.sort(key = lambda x:(-x[0], -x[1]))
    first = dot.pop()
    dot.sort(key=cmp_to_key(compare))
    dot.append(first)
    stack = [first, dot[0]]
    i = 1
    while i < len(dot):
        while ccw(stack[len(stack)- 2], stack[len(stack) - 1], dot[i]) <= 0:
            stack.pop()
            if len(stack) == 1:
                break
        stack.append(dot[i])
        i += 1
    stack.pop()
    if len(stack) < 3:
        break
    for i in stack:
        dot.remove(i)
        ans[i[2]] = floor
    floor += 1

# 답 출력
print(*ans)