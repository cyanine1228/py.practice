# 세그먼트트리 클래스
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
    
# 라이브러리 세팅
import sys

# 세그먼트트리에 사용할 함수 생성
def sum(a, b):
    return a + b

# 변수 세팅
n, s = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))

# 세그먼트트리 생성
seg = segment(n, sum)       
seg.reset(k)

# 모든 구간합을 구해보며 s와 일치한다면 ans에 1추가
ans = 0
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if seg.find(i, j) == s:
            ans += 1

# 답 출력
print(ans)