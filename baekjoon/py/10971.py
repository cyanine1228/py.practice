import sys                                                  # 빠른 입출력을 위한 sys 라이브러리

n = int(sys.stdin.readline())                               # 도시 수 입력
node = [[]for i in range(n + 1)]                            # 도시 이동경로를 저장할 리스트 추가

for i in range(1, n + 1):                                   # 도시 이동경로 입력력 
    nodet = list(map(int, sys.stdin.readline().split()))    
    for j in range(n):                                      
        if nodet[j] != 0:
            node[j + 1].append([i, nodet[j]])

vi = [True] + [False] * n                                   # 방문 상태 선언
sum = 0                                                     # 비용 선언
ma = 1000000000000000000000000000                           # 최소비용 선언
def dfs(l):                                                 # 모든 도시를 순회하기 위한 함수
    global sum
    global ma
    for i in node[l]:                                       # 현재 순회중인 도시에서 다음도시로 가는 경우의수 탐색
        if (not(False in vi)) & (i[0] == 1) & (i[1] != 0):  # 모든 도시를 순회했고 시작지점으로 돌아가는가?
            sum += i[1]
            if sum < ma:
                ma = sum
            sum -= i[1]
            return
        if vi[i[0]]:                                        # 이미 방문한 도시라면 패스
            continue
        vi[i[0]] = True                                     # 방문할 도시의 방문여부를 참으로 변경
        sum += i[1]                                         # 비용 추가
        dfs(i[0])                                           # 그다음 도시를 기준으로 다시 반복
        sum -= i[1]                                         # 모든 경우의수를 돌았으므로 다시 제거
        vi[i[0]] = False                                    # 방문여부도 다시 거짓으로 변경

vi[1] = True
dfs(1)                            
print(ma)                                                   # 최소비용 출력력