# 라이브러리 세팅
import sys
from functools import cmp_to_key

# ccw함수
def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

# 거리 측정 함수
def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

# 비교 함수
first = None
def compare(a, b):
    k = ccw(first, a, b)
    if k == 0:
        return distance(first, a) - distance(first, b)
    else:
        return -k
    
# 테스트 케이스 수 입력
for P in range(int(sys.stdin.readline())):

    # 변수 세팅
    n = int(sys.stdin.readline())
    a = []
    for i in range((n - 1) // 5 + 1):
        inp = list(map(int, sys.stdin.readline().split()))
        for j in range(0, len(inp), 2):
            a.append([inp[j], inp[j + 1]])
    a.sort(key = lambda x:(x[1], -x[0]))
    first = a.pop()
    a.sort(key = cmp_to_key(compare))
    a.append(first)
    stack = [first, a[0]]

    # 컨벡스 헐 알고리즘으로 볼록껍질 탐색
    i = 1
    while i != len(a):
        while (ccw(stack[len(stack) - 2], stack[len(stack) - 1], a[i]) <= 0) & (len(stack) > 1):
            stack.pop()
        stack.append(a[i])
        i += 1
    stack.pop()

    # 직선인 경우 예외처리
    if len(stack) == 1:
        print(2)
        print(*stack[0])
        print(*a[len(a) - 2])

    # 답 출력
    else:
        print(len(stack))
        print(*stack[0])
        for i in range(len(stack) - 1, 0, -1):
            print(*stack[i])