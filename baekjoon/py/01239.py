# 라이브러리 세팅
import sys
n = int(sys.stdin.readline())

# 변수 세팅
people = list(map(int, sys.stdin.readline().split()))
ma = 0
vi = [False] * n
s = [0]

# 주어진 누적합 리스트에대해 직선의 개수를 반환하는 함수
def line(a):
    ans = 0
    i = 0
    while a[i] < 50:
        if a[i] + 50 in a:
            ans += 1
        i += 1
        if i == len(a):
            break
    return ans

# dfs를 이용해 모든 경우를 탐색하는 함수
def find():
    global ma
    if len(s) == n:
        ma = max(ma, line(s))
        return
    for i in range(n):
        if vi[i]:
            continue
        s.append(people[i] + s[len(s) - 1])
        vi[i] = True
        find()
        vi[i] = False
        s.pop()

# dfs 실행
find() 

# 출력
print(ma)