# 힙 세팅
hip = [None]

# a, b 비교 함수 : a가 위로 올라가야하면 True 반환
def compare(a, b):
    if abs(a) < abs(b):
        return True
    if abs(a) == abs(b):
        if a < b:
            return True
    return False

# 힙[n]을 위로 올리는 함수
def hipup(n):
    if n == 1:
        return
    if compare(hip[n], hip[n // 2]):
        hip[n], hip[n // 2] = hip[n // 2], hip[n]
        hipup(n // 2)

# 힙에 k를 추가하는 함수
def hipadd(k):
    hip.append(k)
    hipup(len(hip) - 1)

# 힙[n]을 아래로 내리는 함수
def hipdown(n):
    if len(hip) <= n * 2:
        return
    if len(hip) <= n * 2 + 1:
        if compare(hip[n * 2], hip[n]):
            hip[n * 2], hip[n] = hip[n], hip[n * 2]
            return
        return
    if compare(hip[n * 2], hip[n * 2 + 1]):
        if compare(hip[n * 2], hip[n]):
            hip[n * 2], hip[n] = hip[n], hip[n * 2]
            hipdown(n * 2)
    else:
        if compare(hip[n * 2 + 1], hip[n]):
            hip[n * 2 + 1], hip[n] = hip[n], hip[n * 2 + 1]
            hipdown(n * 2 + 1)

# 힙의 최상위값을 제거하는 함수
def hipremove():
    if len(hip) == 1:
        return 0
    elif len(hip) == 2:
        return hip.pop()
    k = hip[1]
    hip[1] = hip.pop()
    hipdown(1)
    return k

# 라이브러리 세팅
import sys

# 쿼리 수행
for n in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    if k == 0:
        print(hipremove())
    else:
        hipadd(k)