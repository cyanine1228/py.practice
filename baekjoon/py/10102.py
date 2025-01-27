# n 입력
input()

# 개표결과 입력
lis = list(input())

# 개표수 선언
A = 0
B = 0

# 개표결과 체크
for i in lis:
    if i == "A":
        A += 1
    else:
        B += 1

# 개표수에따라 출력
if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")