a = int(input())        # a 입력    
b = int(input())        # b 입력
c = b                   # 임시로 쓸 c 선언
print(a * (c % 10))     # c의 첫자리수(b의 첫자리수) * a 출력
c //= 10                # c을 10으로 나눔
print(a * (c % 10))     # c의 첫자리수(b의 둘째자리수) * a 출력
c //= 10                # c을 10으로 나눔
print(a * (c % 10))     # c의 첫자리수(b의 셋쨰자리수) * a 출력력
print(a * b)            # a * b 출력