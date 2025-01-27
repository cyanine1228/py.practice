# 누적합 계산
scoresum = [0]
for i in range(10):
    scoresum.append(scoresum[i] + int(input()))

# 답 계산
ans = 0
k = 100
for i in range(10, -1, -1):
    if abs(scoresum[i] - 100) < k:
        ans = scoresum[i]
        k = abs(scoresum[i] - 100)

# 출력
print(ans)
