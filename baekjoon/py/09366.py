# 테스트 케이스 수 입력
for i in range(1, int(input()) + 1):

    # 세 변 입력, 정렬
    l = list(map(int, input().split()))
    l.sort()

    # 출력
    print("Case #{}: ".format(i), end = "")
    if l[0] + l[1] <= l[2]:
        print("invalid!")
    elif l[0] == l[1] == l[2]:
        print("equilateral")
    elif (l[0] == l[1]) | (l[1] == l[2]):
        print("isosceles")
    else:
        print("scalene")
    