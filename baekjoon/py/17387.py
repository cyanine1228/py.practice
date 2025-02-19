# 라이브러리 세팅
import sys

# ccw 함수
def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

# 변수 세팅
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
one = [x1, y1]
two = [x2, y2]
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
three = [x3, y3]
four = [x4, y4]

# 예외처리(같은 직선상에 있는 경우)
if (ccw(one, two, three) == 0) & (ccw(one, two, four) == 0) & (ccw(three, four, one) == 0) & (ccw(three, four, two) == 0):
    line_1 = [one, two] 
    line_2 = [three, four]
    line_1.sort(key=lambda x:(x[0]))
    line_2.sort(key=lambda x:(x[0]))
    if (line_1[0][0] > line_2[1][0]) | (line_1[1][0] < line_2[0][0]):
        print(0)
        exit(0)
    line_1.sort(key=lambda x:(x[1]))
    line_2.sort(key=lambda x:(x[1]))
    if (line_1[0][1] > line_2[1][1]) | (line_1[1][1] < line_2[0][1]):
        print(0)
        exit(0)
    else:
        print(1)
        exit(0)

# ccw를 이용하여 답 탐색
if (ccw(one, two, three) * ccw(one, two, four) <= 0) & (ccw(three, four, one) * ccw(three, four, two) <= 0):
    print(1)
else:
    print(0)