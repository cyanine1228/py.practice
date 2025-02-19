# 입력, 대각선 길이의 제곱을 k에 저장
n, w, h = map(int, input().split())
k = w ** 2 + h ** 2

# 쿼리 수행
for i in range(n):

    # 입력
    l = int(input())

    # 만약 대각선길이보다 입력값이 작다면 DA, 크다면 NE 출력
    if l ** 2 <= k:
        print("DA")
    else:
        print("NE")