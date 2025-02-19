# 세그먼트 트리 클래스
# 처음 선언시 크기와 사용할 함수를 입력(합, 최대값, 최소값 등등)
# reset을 통해 세그먼트 트리 생성, 초기화
# modify를 통해 수정
# find를 통해 구간내 조건(위에 입력한 함수)에 해당하는 값 출력

class segment:

    def __init__(self, size, function):
        self.tree = [None] * (size * 4)
        self.f = function
        self.size = size

    def inmodify(self, nowindex_start, nowindex_end, nowpointer, targetindex, value):
        if nowindex_start == nowindex_end:
            if nowindex_start == targetindex:
                self.tree[nowpointer] = value
                return
            else:
                return
        if nowindex_start <= targetindex <= nowindex_end:
            self.inmodify(nowindex_start, (nowindex_start + nowindex_end) // 2, nowpointer * 2, targetindex, value)
            self.inmodify((nowindex_start + nowindex_end) // 2 + 1, nowindex_end, nowpointer * 2 + 1, targetindex, value)
            if (self.tree[nowpointer * 2] == None) | (self.tree[nowpointer * 2 + 1] == None):
                return
            self.tree[nowpointer] = self.f(self.tree[nowpointer * 2], self.tree[nowpointer * 2 + 1])
    
    def modify(self, targetindex, value):
        self.inmodify(1, self.size, 1, targetindex, value)
        return

    def infind(self, nowindex_start, nowindex_end, nowpointer, targetindex_start, targetindex_end):
        if targetindex_start <= nowindex_start <= nowindex_end <= targetindex_end:
            return self.tree[nowpointer]
        if (targetindex_end < nowindex_start) | (targetindex_start > nowindex_end):
            return None
        a = self.infind(nowindex_start, (nowindex_start + nowindex_end) // 2, nowpointer * 2, targetindex_start, targetindex_end)
        b = self.infind((nowindex_start + nowindex_end) // 2 + 1, nowindex_end, nowpointer * 2 + 1, targetindex_start, targetindex_end)
        if a == None:
            return b
        if b == None:
            return a
        return self.f(a, b)
    
    def find(self, targetindex_start, targetindex_end):
        if targetindex_start > targetindex_end:
            targetindex_start, targetindex_end = targetindex_end, targetindex_start
        return self.infind(1, self.size, 1, targetindex_start, targetindex_end)
    
    def reset(self, afterlist):
        for i in range(self.size):
            self.modify(i + 1, afterlist[i])
        return

# 합 함수
def sum(a, b):
    return a + b

# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
seg = segment(n, sum)
seg.reset(list(map(int, sys.stdin.readline().split())))
q = []
i = 1
j = 1

# 쿼리 세팅(정렬)
for M in range(int(sys.stdin.readline())):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        q.append([com[0]] + [i] + [com[1], com[2], 10000000000000])
        i += 1
    else:
        q.append(com + [j])
        j += 1
q.sort(key = lambda x:(x[1], x[0]))

# 쿼리 수행
ans = []
for com in q:
    if com[0] == 1:
        seg.modify(com[2], com[3])
    else:
        ans.append([com[4], seg.find(com[2], com[3])])

# 답 정렬
ans.sort(key = lambda x:x[0])

# 답 출력
for i in ans:
    print(i[1])