# 라이브러리 세팅
import sys

# 변수 세팅
m = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

# 모든값을 xor시켜서 ans에 저장(스프라그 그런디 정리)
ans = p[0]
for i in range(1, m):
    ans ^= p[i]

# ans가 0인지(패배) 확인후 답 출력
if ans == 0:
    print("cubelover")
else:
    print("koosaga")