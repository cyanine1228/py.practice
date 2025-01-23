# 라이브러리 세팅
import sys

# 기본 변수 세팅
inven = []
s = []

# 백트래킹 함수 구현
def backk(l):

    # 길이가 6이됐다면 출력
    if len(s) == 6:
        print(*s)
        return
    
    # 아니라면 다음숫자 추가
    for i in range(l, len(inven)):
        s.append(inven[i])
        backk(i + 1)
        s.pop()

# 무한 반복
while True:
    
    # 입력후 입력이 0 이라면 탈출
    inven = list(map(int, sys.stdin.readline().split()))
    if inven[0] == 0:
        break

    # 아니라면 백트래킹 함수에따라 출력
    inven.pop(0)
    backk(0)
    print()
