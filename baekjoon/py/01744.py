import sys                                          # 빠른 입출력을 위한 sys 라이브러리
n = int(sys.stdin.readline())                       # 수열의 길이 저장
lis = []                                            # 수열 선언
for i in range(n):                                  # n회 반복하여 수열 입력
    lis.append(int(sys.stdin.readline()))           # 수열 입력
lis.sort()                                          # 수열 정렬
i = 0                                               # 수열을 음수수열, 0수열, 양수수열로 나누기 위한 준비
while lis[i] < 0:                                   # 현재 수열의 값이 음수인 동안
    i += 1                                          # 현재 위치 + 1
    if len(lis) == i:                               # 만약 수열의 길이와 현재위치가 일치한다면(수열이 모두 음수라면)
        break                                       # 탈출
listminus = lis[:i]                                 # 음수수열을 선언
if len(lis) != i:                                   # 만약 수열이 전부 음수가 아니라면
    if lis[i] == 0:                                 # 만약 수열에 0이 존재한다면
        j = i + 1                                   # 양수를 찾기위해 j 선언
        if len(lis) == j:                           # j가 수열의 길이라면(수열에 양수가 없다ㅕㄴ)
            listzero = [0]                          # 제로는 [0]
            listplus = []                           # 플러스는 존재 x
        while lis[j] == 0:                          # 수열의 탐색값이 0인동안
            j += 1                                  # j에 1 추가
            if len(lis) == j:                       # 만약에 j가 수열 길이와 같다면(양수가 없다면)
                break                               # 탈출
        if len(lis) == j:                           # 만약에 j가 수열 길이오아 같다면(양수가 없다면)
            listzero = [0]                          # 제로는 [0] (실제로는 [0, 0, 0]과 같은 꼴이나 의미없으므로 [0]으로 통일일)
            listplus = []                           # 플러스는 존재 x
        else:                                       # 만약 양수가 존재한다면
            listzero = lis[i:j]                     # 모든 0값은 제로에 저장
            listplus = lis[j:]                      # 그 이후 양수값은 플러스에 저장
    else:                                           # 0이 존재하지 않으므로 제로는 비우고 나머지는 플러스에 추가
        listzero = []                               # 제로는 존재 x
        listplus = lis[i:]                          # 양수는 음수 이외 값 전부를 가짐
else:                                               # 만약에 음수만 있다면
    listzero = []                                   # 제로는 존재 x 
    listplus = []                                   # 플러스도 존재 x
listplus.reverse()                                  # 큰값을 쉽게 찾기위해 플러스를 리버스
sum = 0                                             # 합을 0으로 설정 
if len(listplus) % 2 == 1:                          # 만약에 플러스수열의 길이가 홀수라면
    listplus.append(1)                              # 편의를 위해 1추가
    sum -= 1                                        # 이후 덧셈과정에도 1이 추가돼돼버리므로 최종값에 -1
for i in range(0, len(listplus), 2):                # 플러스 값을 통한 연산과정 : 9 8 7 4 2 1 ..... 같은 식이 있을때 첫번째와 두번째, 세번째와 네번째....가 최고값인걸 이용
    if listplus[i + 1] == 1:                        # 만약 곱해야할 두값중에 1이 있다면 : n * 1보다 n + 1이 더 크므로 따로 연산
        sum += listplus[i] + listplus[i + 1]        # 각값의 합을 최종합에 덧셈(이 과정때문에 앞에서 1 추가시 합에 -1을 하였음)
    else:                                           # 아닌경우
        sum += listplus[i] * listplus[i + 1]        # 곱을 최종합에 덧셈
if len(listminus) % 2 == 1:                         # 마이너스가 홀수개인 경우
    if len(listzero) != 0:                          # 남는 한개의 마이너스를 0이 상쇄할 수 있다면  
        listminus.pop()                             # 상쇄
    else:                                           # 안된다면
        sum += listminus.pop()                      # 그만큼 감소
for i in range(0, len(listminus), 2):               # 마이너스도 두개씩 묶으면 플러스로 치환되므로 위와 똑같은 과정을 반복
    sum += listminus[i] * listminus[i + 1]          # 곱을 최종합에 덧셉
print(sum)                                          # 최종합 출력