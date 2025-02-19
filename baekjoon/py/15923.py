# 변수 세팅
n = int(input())
a = list(map(int, input().split()))
b = list(a)
ans = 0

# 라인 길이 구하기
for i in range(n - 1):
    c = list(map(int, input().split()))
    ans += abs(b[0] - c[0]) + abs(b[1] - c[1])
    b = list(c)
ans += abs(a[0] - b[0]) + abs(a[1] - b[1])

# 출력
print(ans)