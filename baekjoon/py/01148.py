# 라이브러리 세팅
import sys

# 사전 세팅
st = []
while True:
    i = list(sys.stdin.readline().strip())
    if i[0] == "-":
        break
    st.append(i)

# 답 탐색
while True:

    # 퍼즐판 입력
    s = list(sys.stdin.readline().strip())

    # 종료 처리
    if s[0] == "#":
        break

    # 탐색할 문자열이 퍼즐판내에서 구성 가능한지에 대한 여부를 확인하기 위한 수열
    snum = [0] * 26
    for i in s:
        snum[ord(i) - 65] += 1
    
    # 답을 탐색하기 위한 수열
    ans = [0] * 26

    # 사전속 문자열을 순회하며 탐색 
    for k in st:

        # snum을 복사
        tnum = list(snum)

        # 현재 탐색중인 문자열에 포함되는 문자를 저장할 집합
        an = set()

        # 문자열내의 문자 순회
        for l in k:

            # 만약 문자열 구성이 불가능하다면 탈출
            if tnum[ord(l) - 65] == 0:
                break

            # 현재 문자번호의 tnum을 -1, an에 현재문자 추가
            tnum[ord(l) - 65] -= 1
            an.add(ord(l) - 65)

        # 문자열 구성이 불가능하다면 ans에서 an에 있는 문자들의 번호에 +1
        else:
            for p in an:
                ans[p] += 1

    # 최대 최소 탐색
    mi = 10000000000
    ma = -1
    for i in range(26):
        if not(chr(i + 65) in s):
            continue
        if ans[i] < mi:
            mi = ans[i]
        if ans[i] > ma:
            ma = ans[i]

    # 최대 최소값과 일치하는지 확인후 조건에 따라 출력
    for i in range(26):
        if not(chr(i + 65) in s):
            continue
        if ans[i] == mi:
            print(chr(i + 65), end = "")
    print(" {}".format(mi), end = " ")
    for i in range(26):
        if not(chr(i + 65) in s):
            continue
        if ans[i] == ma:
            print(chr(i + 65), end = "")
    print(" {}".format(ma))