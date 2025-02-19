# 라이브러리 세팅
import sys
from functools import cmp_to_key

# a를 중심으로 c가 b보다 오른쪽에 있는지, 만약 같은직선위에 있다면 거리가 가까운지 반환하는 함수 
def right(a, b, c):
    k = (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])
    if k == 0:
        return ((b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2) - ((c[1] - a[1]) ** 2 + (c[0] - a[0]) ** 2)
    return -k
def line(a, b, c):
    if (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]):
        return True
    return False
# 테스트 케이스 수 입력
for T in range(int(sys.stdin.readline())):

    # 변수 세팅 
    d = list(map(int, sys.stdin.readline().split()))
    dot = []
    for i in range(d[0]):
        dot.append([d[i * 2 + 1], d[i * 2 + 2], i])
    dot.sort(key = lambda x:(x[1], x[0]))
    first = dot.pop(0)

    # 비교함수
    def so(a, b):
        return right(first, a, b)
    
    # 정렬
    dot.sort(key = cmp_to_key(so))
    i = 1

    # 마지막 점들이 일직선에 있는경우를 예외처리
    while line(first, dot[len(dot) - 1], dot[len(dot) - i]):
        i += 1
    i -= 1
    k = dot[len(dot) - i:]
    k.reverse()
    dot = dot[:len(dot) - i] + k
    
    # 출력
    print(first[2], end = " ")
    for i in dot:
        print(i[2], end = " ")
    print("")