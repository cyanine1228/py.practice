# 테스트 케이스 입력
for T in range(int(input())):

    # 점수 초기화
    y, k = 0, 0

    # 점수 추가
    for i in range(9):
        a, b = map(int, input().split())
        y += a
        k += b

    # 조건에 따라 출력
    if y > k:
        print("Yonsei")
    elif y < k:
        print("Korea")
    else:
        print("Draw")