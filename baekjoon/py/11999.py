# 변수 세팅
x, y, m = map(int, input().split())
ma = 0

# 모든 경우 탐색
for i in range(0, m + 1, x):
    res = m - i
    res %= y
    res = m - res
    ma = max(ma, res)

# 출력
print(ma)