# 변수 세팅
ans = [0]
sq = []
i = 1
while i ** 2 <= 50000:
    sq.append(i ** 2)
    i += 1
n = int(input())

# 값 탐색 : 현재 탐색중인 값에서 제곱수만큼 뺀값들의 정답의 최소값 + 1
for i in range(1, n + 1):
    j = 0
    mi = 5
    while i - sq[j] >= 0:
        mi = min(mi, ans[i - sq[j]] + 1)
        j += 1
        if j == len(sq):
            break
    ans.append(mi)

# 답 출력
print(ans[n])