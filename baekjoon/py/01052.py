# n, k 입력
n, k = map(int, input().split())

# n값을 2의 제곱수들의 합으로 변환하여 a에 저장(내림차순)
i = 0
while 2 ** i <= n:
    i += 1
a = []
while n > 0:
    if 2 ** i <= n:
        a.append(2 ** i)
        n -= 2 ** i
    i -= 1

# a의 길이가 k보다 큰동안 가장 작은 두수의 차를 ans에 더하고 두 수중 더 큰수를 두배로 올림
ans = 0
while len(a) > k:
    ans += a[len(a) - 2] - a.pop()
    a[len(a) - 1] *= 2 

# 답 출력
print(ans)