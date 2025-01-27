# 두 수 입력
n, m = map(int, input().split())

# 무한 반복
while True:

    # 상대에게 추가후 5를 넘는다면 게임 종료
    m += n
    if m >= 5:
        print("yt")
        exit(0)

    # 나에게 추가후 5를 넘는다면 게임 종료
    n += m
    if n >= 5:
        print("yj")
        exit(0)