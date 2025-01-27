# 무한 반복
while True:

    # 입력
    a, b = map(int, input().split())

    # 둘다 0이면 탈출
    if a == b == 0:
        break

    # a + b출력
    print(a + b)