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

# 변수 세팅, 세그먼트 초기화
n, q = map(int, sys.stdin.readline().split())
seg = segment(n, sum)
seg.reset(list(map(int, sys.stdin.readline().split())))

# 쿼리 시행
for i in range(q):
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(seg.find(a, b))
    seg.modify(c, d)