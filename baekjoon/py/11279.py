# 라이브러리 세팅
import sys

# 힙 세팅
hip = [None]

# n에 저장된 힙을 조건에따라 올리는 함수
def hipup(n):
    if n == 1:
        return
    if hip[n] > hip[n // 2]:
        hip[n], hip[n // 2] = hip[n // 2], hip[n]
        hipup(n // 2)

# 힙에 k추가
def hipadd(k):
    hip.append(k)
    hipup(len(hip) - 1)

# n에 저장된 힙을 조건에따라 내리는 함수
def hipdown(n):
    if (n * 2) >= len(hip):
        return
    if (n * 2 + 1) >= len(hip):
        if hip[n] < hip[n * 2]:
            hip[n * 2], hip[n] = hip[n], hip[n * 2]
        return
    if hip[n * 2] < hip[n * 2 + 1]:
        if hip[n * 2 + 1] > hip[n]:
            hip[n], hip[n * 2 + 1] = hip[n * 2 + 1], hip[n]
            hipdown(n * 2 + 1)
        return
    else:
        if hip[n * 2] > hip[n]:
            hip[n], hip[n * 2] = hip[n * 2], hip[n]
            hipdown(n * 2)

# 힙의 맨위 값을 반환, 제거
def hipremove():
    if len(hip) == 1:
        return 0
    if len(hip) == 2:
        return hip.pop()
    k = hip[1]
    hip[1] = hip.pop()
    hipdown(1)
    return k

# 쿼리 수행
for N in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x == 0:
        print(hipremove())
    else:
        hipadd(x)