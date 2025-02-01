# 라이브러리 세팅 
import sys

# 테스트 케이스 수 입력
for T in range(int(sys.stdin.readline())):

    # 변수 세팅
    n = int(sys.stdin.readline())
    tree = [-10000000000000000] + [None] * (n * 4)

    # 우선순위 큐에 n을 추가하는 함수
    def add (n, index):
        if n <= tree[index]:
            if tree[index * 2] == None:
                tree[index * 2] = n
                return
            else:
                add(n, index * 2)
                return
        else:
            if tree[index * 2 + 1] == None:
                tree[index * 2 + 1] = n
                return
            else:
                add(n, index * 2 + 1)
                return
    
    # 최소값을 제거후 반환 
    def mi(index):
        if tree[index * 2] == None:
            k = tree[index]
            tree[index] = None
            return k
        return mi(index * 2)
    
    # 최대값을 제거후 반환
    def ma(index):
        if tree[index * 2 + 1] == None:
            k = tree[index]
            tree[index] = None
            return k
        return mi(index * 2 + 1)
    
    # 명령 수행
    for N in range(n):

        # 명령 입력
        com = list(sys.stdin.readline().split())

        # 추가 명령
        if com[0] == "I":
            add(int(com[1]), 0)

        # 제거 명령
        else:
            if tree[1] != None:
                if int(com[1]) == 1:
                    ma(1)
                else:
                    mi(1)
    
    # 출력
    if tree[1] != None:
        k = mi(1)
        if tree[1] != None:
            print(ma(1), k)
        else:
            print(k, k)
    else:
        print("EMPTY")