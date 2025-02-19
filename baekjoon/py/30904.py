# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
ans = 0

# i, j번 과일을 남기는 경우
for i in range(1, 9):
    for j in range(i + 1, 10):

        # 변수 세팅
        stack = 0
        res = set()

        # 모든 칸 순회
        for k in s:

            # 현재 순회중인 칸이 남기는 과일에 해당하는경우 연속된 과일의 길이(stack)에 +1
            if (k == i) | (k == j):
                stack += 1

            # 해당하지 않는경우 stack을 res에 추가후 초기화
            else:
                res.add(stack)
                stack = 0
        res.add(stack)

        # res중 가장 큰값과 ans를 비교, ans갱신
        res = list(res)
        res.sort()
        ans = max(ans, res.pop())

# 답 출력
print(ans)