# 답을 저장할 변수 선언
ans = [0, 0, 0, 0, 0]

# 테스트 케이스 입력
for T in range(int(input())):

    # x y 입력
    x, y = map(int, input().split())

    # 조건에 따라 답에 1 추가
    if (x == 0) | (y == 0):
        ans[4] += 1
    elif x > 0:
        if y > 0:
            ans[0] += 1
        else:
            ans[3] += 1
    else:
        if y > 0:
            ans[1] += 1
        else:
            ans[2] += 1

# 답 출력
for i in range(4):
    print("Q{}: {}".format(i + 1, ans[i]))
print("AXIS:", ans[4])