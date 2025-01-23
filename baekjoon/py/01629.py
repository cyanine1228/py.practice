# 분할 정복을 이용한 거듭제곱 함수(a ** b mod c)
def po(a, b, c):

    # 1승이라면 a % c 반환
    if b == 1:
        return a % c
    
    # b가 홀수라면 a ** b == ((a ** (b // 2)) ** 2) * a 임을 이용해서 a ** b mod c를 반환
    if b % 2 == 1:
        return (((po(a, b // 2, c) % c) ** 2) * (a % c)) % c
    
    # b가 짝수라면 a ** b == ((a ** (b // 2)) ** 2) 임을 이용해서 a ** b mod c를 반환
    return ((po(a, b // 2, c) % c) ** 2) % c

# a, b, c 입력후 답 출력
a, b, c = map(int, input().split())
print(po(a, b, c))