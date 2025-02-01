# 라이브러리 세팅
import sys

# 테스트 케이스 수 입력
for T in range(int(sys.stdin.readline())):

    # 변수 세팅
    n = int(sys.stdin.readline())
    dic = {}

    # 딕셔너리 생성
    for N in range(n):
        com = list(sys.stdin.readline().split())
        if dic.get(com[1], "x") == "x":
            dic[com[1]] = 2
        else:
            dic[com[1]] += 1

    # 딕셔너리를 이용하여 답 출력
    sum = 1
    for k in dic.values():
        sum *= k
    print(sum - 1)