# 라이브러리 세팅
import sys

# 테스트 케이스 수 입력
for T in range(int(sys.stdin.readline())):

    # 변수 세팅
    n = int(sys.stdin.readline())
    k = 2

    # k의 최소값을 찾고, 그 값에따른 정답 출력
    while k * (k + 1) // 2 <= n:
        if (n - (k * (k + 1) // 2)) % k == 0:
            p = (n - (k * (k + 1) // 2)) // k
            ans = list(range(1 + p, k + p + 1))
            print(n, "=", " + ".join(map(str, ans)))
            break
        k += 1

    # 가능한 k가 없다면 불가능 출력
    else:
        print("IMPOSSIBLE")