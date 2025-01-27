# 점수 합
sum = 0

# 5회 반복
for i in range(5):

    # 입력
    score = int(input())

    # 40점 이하라면 40점으로 고정
    if score < 40:
        score = 40

    # 합에 점수를 덧셈
    sum += score

# 합 / 5 출력
print(sum // 5)