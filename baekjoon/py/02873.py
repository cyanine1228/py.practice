import sys                                                          # 빠른 입출력을 위한 sys 라이브러리
r, c = map(int, sys.stdin.readline().split())                       # R값과 C값 입력력
board = []                                                          # 문제풀이에 사용할 가중치(기쁨) 저장 보드
for i in range(r):                                                  # R회 반복하여 보드를 입력
    board.append(list(map(int, sys.stdin.readline().split())))      # 보드 입력
if r % 2 == 1:                                                      # 만약 세로축이 홀수칸이라면(ㄹ자 형태로 모든칸을 지날수 있음)
    print("R" * (c - 1), end = "")                                  # 오른쪽 끝으로 가는 명령
    for i in range(r // 2):                                         # 그뒤로부터 남은 세로칸 // 2회만큼 반복
        print("D" + "L" * (c - 1) + "D" + "R" * (c - 1), end = "")  # ㄷ자 형태로 가는 명령
    exit(0)                                                         # 탈출
if c % 2 == 1:                                                      # 가로축이 홀수칸인 경우(90도 회전하면 같으므로 생략략)
    print("D" * (r - 1), end = "")
    for i in range(c // 2):
        print("R" + "U" * (r - 1) + "R" + "D" * (r - 1), end = "")
    exit(0)

# 양변이 둘다 짝수인경우:

# 만약 왼쪽 위 첫번째칸을 체스판의 흰칸이라 둔다면 항상 검은칸 한칸만을 피하여 가는 방법이 존재함
# ㄴ 왜냐? 보드를 세로 두칸단위로 자른후에 피할 검은칸을 포함한 부분을 제외하고는 ㄷ이나 그 반대모양으로,
# 포함한 부분은 한칸씩 업다운하며 지그재그로 가면 되기 때문
# 예)

# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 0 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1

# 0을 피하기 위한 방법은 DRURRDRURDDLLLLLDRRRRRDLLLLLDRRRRRR

# 그러나 만약 흰칸 중에 검은칸보다 가중치가 낮은칸이 있고 그 한칸만을 피할 방법이 있다면?
# 아쉽게도 그런경우는 존재하지 않는다. 어떤 경우든 검은칸 한칸은 무조건 피해야 한다
# 왜냐? 현재 흰칸과 검은칸의 수는 동일하다. 또한 매 입력마다 흰칸과 검은칸을 번갈아 가며 지난다
# 이런상황에서 시작과 마지막은 둘다 흰칸이므로 이동 순서는 흰검흰검...검흰검흰이 된다
# 이때 총 이동순서에서 흰칸이 검은칸보다 한칸 많으므로 검은칸 하나는 무조건적으로 지나지 않아야 한다
# 즉 양변이 둘다 짝수라면 검은칸의 값중 최소값 한칸만을 피하는 답을 출력하면 된다

mi = 10000                                                                  # 초기 최소값(다음에 어떤값이오든 그 값이 더 작도록 10000으로 설정)
mix = -1                                                                    # 초기 최소값을 가리키는 x값(-1로 초기화)
miy = -1                                                                    # 초기 최소값을 가리키는 y값(-1로 초기화)
for i in range(r):                                                          # i행 탐색을 위해 반복
    for j in range(c):                                                      # j열 탐색을 위해 반복
        if (board[i][j] < mi) & (i + j) % 2 == 1:                           # i행 c열이 가리키는 값이 최소값보다 작고 그 칸이 위에 언급한 "검은칸" 이라면면
            mi = board[i][j]                                                # 최소값 변경
            mix = i                                                         # x값도 변경
            miy = j                                                         # y값도 변경

# 기본 알고리즘은 위에서 말한대로 보드를 세로 두칸단위로 잘라 실행
# 이후는 가능한 경우의 수를 나눠 출력한 누더기 코드이므로 설명 생략

tr = True                                                                   
for i in range(0, r, 2):
    if (mix == i) | (mix == i + 1):
        downup = "down"
        tr = False
        if i != 0:
            print("D", end = "")
        for j in range(miy):
            if downup == "down":
                print("DR", end = "")
                downup = "up"
            else:
                print("UR", end = "")
                downup = "down"
        if (miy != c - 1):
            print("R", end = "")
            for j in range(c - miy - 2):
                if downup == "down":
                    print("DR", end = "")
                    downup = "up"
                else:
                    print("UR", end = "")
                    downup = "down"
            print("D", end = "")
    else:
        if tr:
            if i == 0:
                print("R" * (c - 1) + "D" + "L" * (c - 1), end = "")
            else:
                print("D" + "R" * (c - 1) + "D" + "L" * (c - 1), end = "")
        else:
            print("D" + "L" * (c - 1) + "D" + "R" * (c - 1), end = "")