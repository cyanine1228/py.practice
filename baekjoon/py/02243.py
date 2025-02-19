# 라이브러리 세팅
import sys

# 세금먼트 세팅
seg = [0] * 4000000 

# 쿼리 수 세팅
for N in range(int(sys.stdin.readline())):

    # 쿼리 입력
    com = list(map(int, sys.stdin.readline().split()))

    # 추가 쿼리 시행
    if com[0] == 2:
        s = 1
        e = 1000000
        n = 1
        target = com[1] 
        size = com[2]
        while True:
            seg[n] += size
            if s == e:
                break
            if s <= target <= (s + e) // 2:
                e = (s + e) // 2
                n *= 2
            else:
                s = (s + e) // 2 + 1
                n = n * 2 + 1
    
    # 탐색 쿼리 시행
    else:
        s = 1
        e = 1000000
        n = 1
        index = com[1]
        while True:
            seg[n] -= 1
            if s == e:
                print(s)
                break
            if index <= seg[n * 2]:
                e = (s + e) // 2
                n *= 2
            else:
                index -= seg[n * 2]
                s = (s + e) // 2 + 1
                n = n * 2 + 1