import sys
n = int(sys.stdin.readline())                                   # 일정표 수
time = []                                                       # 일정표 저장 리스트
for i in range(n):                                              # 일정표 수만큼 반복
    time.append(list(map(int, sys.stdin.readline().split())))   # 일정표 입력
time.sort(key=lambda x:(x[0], x[1]))                            # 일정표를 시작하는시간에 따라, 같다면 끝나는 시간에 따라 정렬
stack = [time[0]]                                               # 최종 일정표(회의수가 최대가 되는 일정표표)
for i in range(1, len(time)):                                   # 모든 일정표를 돌 동안 반복
    if time[i][0] >= stack[len(stack) - 1][1]:                  # 다음 탐색 일정 시작시간이 최종 일정표의 마지막 일정 보다 늦다면
        stack.append(time[i])                                   # 추가
    elif time[i][1] <= stack[len(stack) - 1][1]:                # 다음 탐색 일정 끝시간이 최종 일정표의 마지막 일정에 포함된다면면
        stack.pop()                                             # 최종일정표의 마지막 일정 제거
        stack.append(time[i])                                   # 다음 탐색 일정을 최종 일정표에 추가
print(len(stack))                                               # 최종 일정표의 길이(회의의 수) 출력