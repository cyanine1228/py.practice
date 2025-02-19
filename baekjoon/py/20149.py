# 라이브러리 세팅
import sys
import math

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
    if line_1[0][0] != line_1[1][0]:
        if (line_1[0][0] > line_2[1][0]) | (line_1[1][0] < line_2[0][0]):
            print(0)
            exit(0)
        if (line_1[0][0] == line_2[1][0]):
            print(1)
            print(*line_1[0])
            exit(0)
        if (line_1[1][0] == line_2[0][0]):
            print(1)
            print(*line_1[1])
            exit(0)
    else:
        line_1.sort(key=lambda x:(x[1]))
        line_2.sort(key=lambda x:(x[1]))
        if (line_1[0][1] > line_2[1][1]) | (line_1[1][1] < line_2[0][1]):
            print(0)
            exit(0)
        if (line_1[0][1] == line_2[1][1]):
            print(1)
            print(*line_1[0])
            exit(0)
        if (line_1[1][1] == line_2[0][1]):
            print(1)
            print(*line_1[1])
            exit(0)
    print(1)
    exit(0)

# ccw를 이용하여 답 탐색
if (ccw(one, two, three) * ccw(one, two, four) <= 0) & (ccw(three, four, one) * ccw(three, four, two) <= 0):

    # 연립방정식을 세우기 위한 변수
    a = [y2 - y1, x2 - x1, x2 * y1 - x1 * y2]
    b = [y4 - y3, x4 - x3, x4 * y3 - x3 * y4]

    # 선분이 x축또는 y축과 평행한경우 예외처리
    if x1 == x2:
        last_x = x1
        last_y = (b[0] * last_x + b[2]) / b[1]
    elif x3 == x4:
        last_x = x3
        last_y = (a[0] * last_x + a[2]) / a[1]
    elif y1 == y2:
        last_y = y1
        last_x = (b[1] * last_y - b[2]) / b[0]
    elif y3 == y4:
        last_y = y3
        last_x = (a[1] * last_y - a[2]) / a[0]

    # 교점 탐색
    else:
        last_x = (a[1] * b[2] - a[2] * b[1]) / (a[0] * b[1] - a[1] * b[0])
        last_y = (a[0] * last_x + a[2]) / a[1]

    # 답 출력
    print(1)
    print(last_x, last_y)
else:
    print(0)