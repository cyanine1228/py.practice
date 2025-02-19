# 라이브러리 세팅
import sys

# 변수 기본 세팅
n = int(sys.stdin.readline())
inf = 1000000000000000
r, g, b = map(int, sys.stdin.readline().split())
R = [r, inf, inf]
G = [inf, g, inf]
B = [inf, inf, b]

# DP를 활용 
for i in range(n - 2):
    r, g, b = map(int, sys.stdin.readline().split())
    R = [min(R[1], R[2]) + r, min(R[0], R[2]) + g, min(R[0], R[1]) + b]
    G = [min(G[1], G[2]) + r, min(G[0], G[2]) + g, min(G[0], G[1]) + b]
    B = [min(B[1], B[2]) + r, min(B[0], B[2]) + g, min(B[0], B[1]) + b]
r, g, b = map(int, sys.stdin.readline().split())
R = [inf, min(R[0], R[2]) + g, min(R[0], R[1]) + b]
G = [min(G[1], G[2]) + r, inf, min(G[0], G[1]) + b]
B = [min(B[1], B[2]) + r, min(B[0], B[2]) + g, inf]

# 답 출력
print(min(R[0], R[1], R[2], G[0], G[1], G[2], B[0], B[1], B[2]))

