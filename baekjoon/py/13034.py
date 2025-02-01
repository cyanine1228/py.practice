# 기본 그런디수
win = [0, 0, 1, 1]

# n 입력
n = int(input())

# mex연산 함수
def mex(a):
    i = 0
    while True:
        if i in a:
            i += 1
        else:
            return i
        
# i입력시 그런디수(win[i])를 추가해가며 win[n]을 탐색, 출력
for i in range(4, n + 1):

    # 만들 수 있는 그런디 수를 저장할 집합 선언
    grundy = set()

    # 그런디 집합에 만들 수 있는 그런디 수 저장
    for j in range(i - 2):
        grundy.add(win[j] ^ win[i - 2 - j])

    # mex 그런디로 현재 상태의 그런디 수 저장
    win.append(mex(grundy))

# 만약 n상태에서의 그런디수가 0이라면 패배, 아니면 승리 출력
if win[n] == 0:
    print(2)
else:
    print(1)