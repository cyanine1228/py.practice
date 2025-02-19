# 테스트 케이스 수 입력
for N in range(1, int(input()) + 1):

    # 입력, 정렬
    l = list(map(int, input().split()))
    l.sort()

    # 출력
    print("Scenario #{}:".format(N))
    if l[0] ** 2 + l[1] ** 2 == l[2] ** 2:
        print("yes")
    else:
        print("no")
    print("")