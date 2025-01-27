# 답을 저장할 변수
sum = 0

# 테스트 케이스 입력 
for _ in range(int(input())):

    # 단어 입력
    word = input()

    # 만약 OI나 01이 있다면 sum에 +1
    if word.count("01") + word.count("OI") != 0:
        sum += 1

# 답 출력
print(sum)