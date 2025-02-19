# 라이브러리 세팅 
import sys

# 변수 세팅 
n, c = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))
w.sort()

# 한묶음으로 가능한경우, 불가능하며 길이가 1인경우 처리
if c in w:
    print(1)
    exit(0)
if n == 1:
    print(0)
    exit(0)

# 두 묶음으로 가능한 경우, 불가능하며 길이가 2인경우 처리
i = 0
j = 1
while True:
    if w[i] + w[j] == c:
        print(1)
        exit(0)
    elif w[i] + w[j] < c:
        j += 1
    else:
        i += 1
    if (j == n) | (i == j):
        break
if n == 2:
    print(0)
    exit(0)

# 세 묶음으로 해야하는 경우
j = 1
while j < n - 1:
    i = 0
    while i < j:
        sum = w[i] + w[j]
        p = j
        q = n
        while p + 1 != q:
            k = (p + q) // 2
            if sum + w[k] == c:
                print(1)
                exit(0)
            elif sum + w[k] < c:
                p = k
            else:
                q = k
        i += 1
    j += 1

# 불가능한 경우
print(0)