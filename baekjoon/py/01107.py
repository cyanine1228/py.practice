import sys                                                  # 빠른 입출력을 위한 sys 라이브러리
n = int(sys.stdin.readline())                               # 정답값 입력
n_list = list(str(n))                                       # 정답값을 리스트로 변경한 자료
m = int(sys.stdin.readline())                               # 고장난 버튼수 입력
button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]                     # 현재 존재하는 버튼 리스트
error = []                                                  # 고장난 버튼을 입력받을 리스트트
if m != 0:                                                  # 고장난 버튼이 존재 한다면
    error = list(map(int, sys.stdin.readline().split()))    # 고장난 버튼 입력
else:                                                       # 고장난 버튼이 없다면
    print(min(abs(n - 100), len(n_list)))                   # 100번에서 +-로 조작할 횟수 vs 그냥 입력 횟수중 작은것 출력    
    exit(0)                                                 # 탈출
for i in error:                                             # 모든 고장난 버튼을 돌동안 반복
    button.remove(i)                                        # 고장난 버튼 제거
channel = [100]                                             # 기본채널 100번 추가
s = []                                                      # 채널 입력을 저장할 리스트 추가


def dfs():                                                  # n과 한자릿수 차이나는 모든 채널을 구하기 위한 함수 ex) n = 1234라면 세자리부터 다섯자리 숫자까지 전부 구함
    if (abs(len(s) - len(n_list)) <= 1) & (len(s) != 0):    # 만약 n과 s가 한자릿수 차이가 난다면
        channel.append(int("".join(map(str, s))))           # 채널에 추가
        if len(s) - len(n_list) == 1:                       # s가 한자릿수 더 많다면
            return                                          # 더 들어갈 필요 없으므로 리턴
    for i in range(len(button)):                            # 모든 버튼을 돌동안 반복
        s.append(button[i])                                 # 현재 버튼을 채널에 입력
        dfs()                                               # 다음 순회 시작
        s.pop()                                             # 순회가 끝났으므로 현재 버튼을 채널에서 제거


dfs()                                                       # 채널 탐색 실행                                             
channel.sort(reverse = True)                                # 정렬시켜 최소값 탐색색
mi = 100                                                    # 기본 최소값은 100으로 설정
for i in channel:                                           # 가능한 채널값들을 모두 돌동안 반복
    if abs(n - mi) >= abs(n - i):                            # 만약 목표값과의 차가 최소값보다 크다면
        mi = i                                              # 최소값 갱신                                                 
print(min(abs(mi - n) + len(list(str(mi))), abs(100 - n)))  # 그 채널을 입력하기까지의 횟수와 +-로 조작해야하는 횟수의 합 또는 100번에서 +-조작 횟수중 작은것을 출력