# 라이브러리 세팅
import sys
import math

# 테스트 케이스 입력
for T in range(int(sys.stdin.readline())):

    # 수와 명령 입력
    com = list(sys.stdin.readline().split())

    # 수 분리후 정확도를 위해 10을 곱한뒤 정수로 변경
    num = float(com.pop(0))
    num *= 10
    num = round(num)

    # 명령에 따라 연산
    for i in com:
        if i == "@":
            num *= 3
        elif i == "%":
            num += 50
        else:
            num -= 70

    # 출력
    print("{}0".format(num / 10))