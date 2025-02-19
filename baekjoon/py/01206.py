# 변수 세팅
n = int(input())
k = []
for i in range(n):
    k.append(int(float(input()) * 1000))
    
# 탐색
i = 1
while True:

    # 현재 인원수(i)로 조건을 만족시킬 수 있는지 탐색 
    for j in k:

        # 만약 오차범위를 포함한 값속에 j값이 없다면(현재 인원수로 해당 평균값을 만들 수 없다면) 탈출
        if not((1000 - 1 * i < j * i % 1000 <= 1000) | ((j * i % 1000) == 0)):
            break

    # 만약 만족 시킬 수 있다면 i출력후 종료
    else:
        print(i)
        exit(0)

    # i에 1 추가
    i += 1