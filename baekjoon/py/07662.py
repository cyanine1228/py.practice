# 라이브러리 세팅
import sys
import heapq

# 테스트 케이스 수 입력
for T in range(int(sys.stdin.readline())):

    # 변수 세팅
    minheap = []
    maxheap = []
    mindel = {}
    maxdel = {}
    mindelnum = 0
    maxdelnum = 0

    # 쿼리 수행
    for K in range(int(sys.stdin.readline())):
        query, n = sys.stdin.readline().split()
        n = int(n)
        if query == "I":
            heapq.heappush(minheap, n)
            heapq.heappush(maxheap, -n)
            if mindel.get(n, "X") == "X":
                mindel[n] = 0
            if maxdel.get(n, "X") == "X":
                maxdel[n] = 0
        else:
            if n == 1:
                while True:
                    if len(maxheap) - maxdelnum <= 0:
                        break
                    k = -heapq.heappop(maxheap)
                    if maxdel[k] > 0:
                        maxdelnum -= 1
                        maxdel[k] -= 1
                    else:
                        mindelnum += 1
                        mindel[k] += 1
                        break
            else:
                while True:
                    if len(maxheap) - maxdelnum <= 0:
                        break
                    k = heapq.heappop(minheap)
                    if mindel[k] > 0:
                        mindelnum -= 1
                        mindel[k] -= 1
                    else:
                        maxdel[k] += 1
                        maxdelnum += 1
                        break

    # 비어있을 경우 
    if len(minheap) - mindelnum <= 0:
        print("EMPTY")
        continue

    # 아닌경우 답 출력
    while True:
        k = -heapq.heappop(maxheap)
        if maxdel[k] > 0:
            maxdel[k] -= 1
        else:
            break
    print(k, end = " ")
    while True:
        k = heapq.heappop(minheap)
        if mindel[k] > 0:
            mindel[k] -= 1
        else:
            break
    print(k)