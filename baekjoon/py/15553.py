# 라이브러리 세팅
import sys

# 변수 세팅
n, k = map(int, sys.stdin.readline().split())
ans = n
b = int(sys.stdin.readline())

# 두 친구사이의 간격을 저장할 리스트 생성
intervel = []
for i in range(n - 1):
    a = int(sys.stdin.readline())
    intervel.append(a - b - 1)
    b = a

# 간격을 시간이 짧은순으로 정렬
intervel.sort()

# 부족한 성냥수만큼 간격이 최소가 되는 간격에서 끄지 않음으로써 최소화
for i in range(n - k):
    ans += intervel[i]

# 답 출력
print(ans)