# 라이브러리 세팅

import sys                               
from collections import deque


# 1000이상 9999이하 소수 집합 만들기

prt = [False, False] + [True] * 10000           # 10000이하 소수 구하기    
pr = []
for i in range(10002):
    if prt[i]:
        pr.append(i)
        for j in range(i * 2, 10002, i):
            prt[j] = False

pr.reverse()                                    # 1000 미만 소수 제거하기
while True:
    if pr.pop() > 1000:
        pr.append(1009)
        break
pr = set(pr)


# 답 계산 과정정

for T in range(int(sys.stdin.readline())):          # 테스트 케이스 수 입력
   
    # 변수 초기화

    sum = 0                                        
    vi = [True] * 10000                             
    n, m = map(int, sys.stdin.readline().split())   
    vi[n] = False
    que = deque([n])


    # 계산과정

    while len(que) != 0:

        if m in que:                                # 변환이 끝났다면 답 출력력
            print(sum)
            break

        for i in range(len(que)):                   # 한자리씩 바꿔가며 큐에 추가
            k = que.popleft()
            k = list(map(int, list(str(k))))
            for j in range(4):
                for l in range(10):
                    p = list(k)
                    p[j] = l
                    p = int("".join(map(str, p))) 
                    if (p in pr) & (vi[p]):
                        vi[p] = False
                        que.append(p)
        sum += 1


    # que가 비었음(더이상 실행가능한 방법이 없음) = Impossible

    else:
        print("Impossible")