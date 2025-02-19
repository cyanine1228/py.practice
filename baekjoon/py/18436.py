# 세그트리 클래스
class segment:

    def __init__(self, size, function):
        self.tree = [None] * (size * 4)
        self.f = function
        self.size = size

    def inmodify(self, nowindex_start, nowindex_end, nowpointer, targetindex, value):
        if nowindex_start == nowindex_end:
            if nowindex_start == targetindex:
                self.tree[nowpointer] = value % 2
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

# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
seg = segment(n, lambda x, y : x + y)
A = list(map(int, sys.stdin.readline().split()))
seg.reset(A)

# 쿼리 수행
m = int(sys.stdin.readline())
for _ in range(m):
    com = list(map(int, sys.stdin.readline().split()))
    if com[0] == 1:
        seg.modify(com[1], com[2])
    elif com[0] == 2:
        print(com[2] - com[1] - seg.find(com[1], com[2]) + 1)
    else:
        print(seg.find(com[1], com[2]))
