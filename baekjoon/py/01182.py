# 라이브러리 세팅
import sys

# 변수 세팅
n, s = map(int, sys.stdin.readline().split())
lis = list(map(int, sys.stdin.readline().split()))
ans = 0
vi = [False] * n
S = []

# dfs 함수 구현
def dfs(l):
    global ans

    # 현재 골라진 부분수열 S의 합 sum이 s와 같고 길이가 0이 아니라면 ans에 +1
    sum = 0
    for i in S:
        sum += i
    if sum == s:
        if len(S) != 0:
            ans += 1

    # 부분수열 S에 추가 할 수 있는 값들을 추가해보며 다시 함수 호출
    for i in range(l, n):
        if vi[i]:
            continue
        vi[i] = True
        S.append(lis[i])
        dfs(i + 1)
        S.pop()
        vi[i] = False

# 함수 실행
dfs(0)

# ans 출력
print(ans)
