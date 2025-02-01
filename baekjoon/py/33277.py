# n, m 입력
n, m = map(int, input().split())

# 경과 시간 계산
k = 60 * 24
k *= m / n
k = int(k)

# 경과 시간을 시와 분으로 나누어 출력
print(str(k//60).zfill(2), str(k%60).zfill(2), sep=":")