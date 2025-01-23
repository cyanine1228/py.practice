# 라이브러리 세팅
import sys

# 집합 세팅(비트마스킹을 이용)
s = 0b000000000000000000000

# 각 명령을 비트마스킹을 이용해 수행
for T in range(int(sys.stdin.readline())):

    com = list(sys.stdin.readline().split())

    if len(com) == 2:
        com[1] = int(com[1])

    if com[0] == "add":
        s = s | (1 << com[1])

    elif com[0] == "remove":
        s = s & ~(1 << com[1])

    elif com[0] == "check":
        if s & (1 << com[1]) != 0:
            print(1)
        else:
            print(0)

    elif com[0] == "toggle":
        s = s ^ (1 << com[1])
        
    elif com[0] == "all":
        s = 0b111111111111111111111
        
    else:
        s = 0b000000000000000000000

