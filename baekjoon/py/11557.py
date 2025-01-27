# 테스트 케이스입력
for T in range(int(input())):

    # 학교명과 술 양을 저장할 리스트 선언
    lis = []

    # 학교명과 술 양을 저장
    for N in range(int(input())):
        school, num = input().split()
        num = int(num)
        lis.append([school, num])

    # 소비한 술에따라 내림차순 정렬
    lis.sort(key=lambda x:-x[1])

    # 첫번째 값의 학교이름을 출력
    print(lis[0][0])