# 라이브러리 세팅
import sys

# 변수 세팅
n, m = map(int, sys.stdin.readline().split())
a = []
for i in range(n):
    st = list(sys.stdin.readline().strip())
    stack = []
    for j in st:
        if j == ".":
            stack.append(1)
        else:
            a.append(len(stack))
            stack = []
    a.append(len(stack))
k = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

# mex함수
def mex(a):
    i = 0
    while i in a:
        i += 1
    return i

# 그런디수 탐색 함수
gr = [0] + [None] * 1000
def grundy(x):
    if gr[x] != None:
        return gr[x]
    i = 0
    a = set()
    while p[i] <= x:
        y = x - p[i]
        for b in range(y + 1):
            d = y - b
            a.add(grundy(b) ^ grundy(d))
        i += 1
        if i == len(p):
            break
    gr[x] = mex(a)
    return gr[x]

# 모든 그런디수를 xor
ans = 0
for i in a:
    ans ^= grundy(i)

# ans 값에 따라 답 출력
if ans == 0:
    print("hyo123bin")
else:
    print("nein")