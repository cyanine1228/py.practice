grundy = [0, 1, 2, 3] + [0] * 3000005
pivo = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
i = 4
while i < 3000001:
    k = 0
    gr = [False] * 100
    while (i - pivo[k]) >= 0:
        gr[grundy[i - pivo[k]]] = True
        k += 1
    k = 0
    while gr[k]:
        k += 1
    grundy[i] = k
    i += 1
import sys
n = int(sys.stdin.readline())
ans = 0
p = list(map(int, sys.stdin.readline().split()))
for i in p:
    ans ^= grundy[i]
if ans == 0:
    print("cubelover")
else:
    print("koosaga")