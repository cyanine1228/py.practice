# n 입력후 조건에 따라 출력
n = list(map(int, input().split()))
n.sort()
print(n[0] * n[2])