import sys
inf = 100000000000000000000
minpower = [inf, inf, inf, inf, inf]
act = list(map(int, sys.stdin.readline().split()))
if len(act) == 2:
    print(2)
    exit(0)
if len(act) == 3:
    