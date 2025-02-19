# 라이브러리 세팅
import sys

# b와 a를 이은직선에서 c가 왼쪽인지, 오른쪽인지 판별하는 함수 
def if_left(a, b, c):
        x1 = b[0] - a[0]
        y1 = b[1] - a[1]
        x2 = c[0] - a[0]
        y2 = c[1] - a[1]
        if x1 * y2 - x2 * y1 > 0:
             return True
        else:
             return False
        
# 변수 세팅
n = int(sys.stdin.readline())
dot = []
for i in range(n):
    dot.append(list(map(int, sys.stdin.readline().split())))
dot.sort(key = lambda x:(-x[1], -x[0]))
first = dot.pop()
dot.sort(key = lambda x:(-(abs(x[0] - first[0]) * (x[0] - first[0]) / ((x[1] - first[1]) ** 2 + (x[0] - first[0]) ** 2)), (x[1] - first[1]) ** 2, (x[0] - first[0]) ** 2))
dot.insert(0, first)
dot.append(first)

# 컨벡스헐 알고리즘
stack = [dot[0], dot[1]]
for i in range(2, n + 1):
    while not(if_left(stack[len(stack) - 2], stack[len(stack) - 1], dot[i])):
         stack.pop()
         if len(stack) == 1:
              break
    stack.append(dot[i])

# 답 출력
print(len(stack) - 1)