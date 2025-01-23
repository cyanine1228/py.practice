# n 입력후 피사노주기에 따라 나눗셈
n = int(input())
n %= 1500000

# 계산후 출력
a, b = 1, 1
for i in range(n - 2):
    a, b = b % 1000000, (a + b) % 1000000

print(b)