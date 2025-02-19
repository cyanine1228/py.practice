# 입력
k = int(input())
d1, d2 = map(int, input().split())

# 출력
print(k ** 2 - ((d2 - d1) / 2) ** 2)