# 라이브러리 세팅
import sys

# 기본 변수 세팅
n = int(sys.stdin.readline())
lis = list(map(int, sys.stdin.readline().split()))
lis.sort()
i = 0
j = n - 1
mi = 100000000000000000000000000
mix = lis[i]
miy = lis[j]

# 투포인터를 활용하여 용액 특성 절대값의 최소값 탐색
while i < j:
    if lis[i] + lis[j] == 0:
        print(lis[i], lis[j])
        exit(0)
    if abs(lis[i] + lis[j]) < mi:
        mi = abs(lis[i] + lis[j])
        mix = lis[i]
        miy = lis[j]
    if lis[i] + lis[j] > 0:
        j -= 1
    else:
        i += 1

# 용액 특성 절대값을 최대로만드는 두 용액 출력
print(mix, miy)