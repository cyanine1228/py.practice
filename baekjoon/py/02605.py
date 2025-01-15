# 라이브러리 세팅
import sys

# 정보 입력 & 기본 변수 선언
n = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))
ans = []

# 답(ans)에 조건대로 사람들을 추가
for i in range(n):
    ans.insert(len(ans) - order[i], i + 1)

# 답 출력
print(" ".join(map(str, ans)))