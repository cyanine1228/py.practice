# 라이브러리 세팅
import sys

# 기본 변수 세팅
n, k = map(int, sys.stdin.readline().split())
s = []
ans = []
vi = [False] * (n + 1)
j = 0

# 백트래킹 함수 세팅
def dfs():

    # 전역변수 선언
    global j

    # 수열이 완성되었고 1과 2가 인접하지 않았다면 
    if (len(s) == n):
        if(abs(s.index(1) - s.index(2)) != 1):

            # 수열 카운트에 1추가, 카운트가 k라면 수열 출력후 종료
            j += 1
            if j == k:
                print(*s)
                exit(0) 
        return
    
    # 다음 함수 시작
    for i in range(1, n + 1):
        if vi[i]:
            continue
        vi[i] = True
        s.append(i)
        dfs()
        s.pop()
        vi[i] = False

# 함수 실행
dfs()