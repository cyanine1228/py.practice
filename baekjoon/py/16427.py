# 입력
n, s = map(int, input().split())
m = list(map(int, input().split()))

# 계산
k = max(m)
k *= s
if k % 1000 != 0:
    k += 1000
k //= 1000

# 출력
print(k)