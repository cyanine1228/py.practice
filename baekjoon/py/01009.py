# 테스트 케이스 입력
for T in range(int(input())):

    # a, b 입력
    a, b = map(int, input().split())

    # 답 탐색
    ans = 1
    for i in range(b):
        ans *= a
        ans %= 10

    # 답 출력
    if ans == 0:
        print(10)
    else:
        print(ans)