# 라이브러리 세팅
import sys

# 기본 변수 세팅
word = sys.stdin.readline().strip()
sum = [[0] * 26]

# 누적합 세팅 : 각 원소가 26개의 숫자로 이루어지며 이 숫자는 역대 나온 각각의 알파벳의 수를 의미하
for i in range(len(word)):
    sum.append(list(sum[i]))
    sum[i + 1][ord(word[i]) - 97] += 1

# 질문을 받고 누적합 리스트를 이용하여 출력
q = int(sys.stdin.readline())
for i in range(q):
    com = list(sys.stdin.readline().split())
    com[0] = ord(com[0]) - 97
    com[1], com[2] = int(com[1]), int(com[2])
    print(sum[com[2] + 1][com[0]] - sum[com[1]][com[0]])