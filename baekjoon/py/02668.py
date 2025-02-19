# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
k = [None]
for i in range(n):
    k.append(int(sys.stdin.readline()))
vi = [False] * (n + 1)
ans = 0
sum = 1
anslist = []
sumlist = []

# 사이클을 찾는 함수수
def cycle(start, now):
    global anslist
    global ans
    global sum
    vi[now] = True
    sumlist.append(now)
    if vi[k[now]] == True:
        if k[now] == start:
            ans += sum
            anslist += sumlist
            return
        else:
            return
    sum += 1
    cycle(start, k[now])

# 존재하는 모든 사이클 찾기
for i in range(1, n + 1):  
    if i in anslist:
        continue
    sum = 1
    sumlist = []
    vi = [False] * (n + 1)
    cycle(i, i)

# 답 출력
print(ans)
anslist.sort()
for i in anslist:
    print(i)