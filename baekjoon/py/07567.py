# 배열 입력
lis = ["start"] + list(input())

# 합계 선언
sum = 0

# 반복
for i in range(1, len(lis)):

    # 만약 현재 탐색중인 글자와 전 글자가 같다면 5추가, 아니면 10추가
    if lis[i] == lis[i - 1]:
        sum += 5
    else:
        sum += 10

# 합계 출력
print(sum)