# 라이브러리 세팅
import sys
import math

# 변수 세팅
n = int(sys.stdin.readline())
size = math.floor(math.sqrt(n)) * 2
A = list(map(int, sys.stdin.readline().split()))
A += [0] * (size - n % size)
B = []
i = 0
while i < len(A):
    k = list(A[i:i + size])
    k.sort()
    B.append(list(k))
    i += size
m = int(sys.stdin.readline())
l = 0

# 이분탐색 함수 세팅
def find(index, k):
    i = -1
    j = len(B[index])
    while i + 1 != j:
        p = (i + j) // 2
        if B[index][p] <= k:
            i = p
        else:
            j = p
    return len(B[index]) - j

# 쿼리 시행
for M in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    i = (a ^ l) - 1
    j = (b ^ l) - 1
    k = c ^ l
    ans = 0
    while (i <= j) & (i % size != 0):
        if A[i] > k:
            ans += 1
        i += 1
    while (i // size < (j + 1) // size) & (i < j):
        ans += find(i // size, k)
        i += size
    while (i <= j):
        if A[i] > k:
            ans += 1
        i += 1
    print(ans)
    l = ans