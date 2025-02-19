# 라이브러리 세팅
import math

# 인덱스
i = 1

# 무한 반복
while True:

    # 입력
    a, b, c = map(int, input().split())

    # 종료 처리
    if a == b == c == 0:
        break

    # 출력
    print("Triangle #{}".format(i))
    if a == -1:
        if c <= b:
            print("Impossible.")
        else:
            print("a = %0.3f" % math.sqrt(c ** 2 - b ** 2))
    elif b == -1:
        if c <= a:
            print("Impossible.")
        else:
            print("b = %0.3f" % math.sqrt(c ** 2 - a ** 2))
    else:
        print("c = %0.3f" % math.sqrt(a ** 2 + b ** 2))
    print(" ")

    # 인덱스 +1
    i += 1