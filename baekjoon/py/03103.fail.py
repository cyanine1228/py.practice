import sys
k, n = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

seg = [0] * (k * 4)
seg = [0, 4, 2, 2, 2, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
def find(s, e, n, i):
    seg[n] += 1
    if s <= i <= (s + e) // 2:
        if s == e:
            return 0
        return find(s, (s + e) // 2, n * 2, i)
    else:
        return find((s + e) // 2 + 1, e, n * 2 + 1, i) + seg[n * 2]
for N in range(n):
    exit(0)

