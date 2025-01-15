import sys                                                  # 빠른 입출력을 위한 sys 라이브러리
n = int(sys.stdin.readline())                               # n 입력
lis = list(map(int, sys.stdin.readline().split()))          # 배열 입력
vi = [False] * n                                            # 방문 여부를 저장할 배열을 추가로 지정
s = []                                                      # 재배열될 배열 s 선언
ma = -10000000000000000                                     # 초기최대값 설정

def dfs():                                                  # 가능한 모든 배열을 찾아 최대값을 구하는 함수
    global ma                                               # ma값 변경을 위해 global
    if len(s) == n:                                         # 만약에 배열이 완성된 배열이라면
        sum = 0                                             # 합은 0 설정
        for i in range(1, len(s)):                          # 배열의 첫번째 빼고 나머지항을 모두 훑으며 반복
            sum += abs(s[i] - s[i - 1])                     # 현재 배열값과 전 배열값의 차만큼 합에 추가
            if sum > ma:                                    # 만약에 합이 최대값보다 크다면
                ma = sum                                    # 최대값을 합으로 설정
    for i in range(n):                                      # 기본 배열을 모두 훑으며 반복
        if vi[i]:                                           # 이미 방문했다면
            continue                                        # 패스
        vi[i] = True                                        # 방문정보를 참으로 변경
        s.append(lis[i])                                    # 재배열될 배열에 기존배열의 i번째 값을 추가
        dfs()                                               # 다시 실행
        s.pop()                                             # 실행이 끝났으므로 방금 추가한 값을 제거
        vi[i] = False                                       # 방문정보도 다시 거짓으로

dfs()                                                       # 함수 실행
print(ma)                                                   # 최대값 출력력