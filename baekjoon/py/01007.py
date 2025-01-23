# 라이브러리 세팅
import sys
import math

# 테스트 케이스 수 입력
for T in range(int(sys.stdin.readline())):

    # 기본 변수 세팅
    n = int(sys.stdin.readline())
    spot = []
    for i in range(n):
        spot.append(list(map(int, sys.stdin.readline().split())))
    possible = []
    mi = 10000000000000000
    num = set()
    for i in range(n):
        num.add(i)
    
    # 벡터매칭의 벡터의 합은 (모든 벡터 도착점 좌표의 합 - 모든 벡터 시작점 좌표의 합)이므로
    # 도착점으로 선택할 n // 2개의 점을 고르고 최소값을 갱신해주는 함수
    def dfs(l):

        # 최소값을 저장할 mi는 광역 선언
        global mi

        # 만약 모두 다 골랐다면 위의 원리에따라 계산후 최소값이라면 갱신
        if len(possible) == n // 2:
            
            spotplus = set(possible)      # 벡터 끝
            spotminus = num - spotplus    # 벡터 시작
            sumx, sumy = 0, 0
            for j in spotplus:
                sumx += spot[j][0]
                sumy += spot[j][1]
            for j in spotminus:
                sumx -= spot[j][0]
                sumy -= spot[j][1]
            if sumx ** 2 + sumy ** 2 < mi:
                mi = sumx ** 2 + sumy ** 2
            return
        
        # 아직 다 안골랐다면 한개를 더 고른 후 다시 함수 실행
        for i in range(l, n):
            possible.append(i)
            dfs(i + 1)
            possible.pop()

    # 위의 함수를 통해 최소값 탐색
    dfs(0)

    # 현재 저장된 최소값은 x ** 2 + y ** 2이므로 루트를 씌워 출력
    print(math.sqrt(mi))