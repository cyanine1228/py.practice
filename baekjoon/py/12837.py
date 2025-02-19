# 라이브러리 세팅 
import sys

# 변수입력, 세그 초기화
n, q = map(int, sys.stdin.readline().split())
seg = [0] * (n * 4)

# 세그 수정함수
def modify(s, e, n, i, p):
    if s <= i <= e:
        if s == e:
            seg[n] += p
            return
        modify(s, (s + e) // 2, n * 2, i, p)
        modify((s + e) // 2 + 1, e, n * 2 + 1, i, p)
        seg[n] = seg[n * 2] + seg[n * 2 + 1]

# 세그 출력함수
def find(s, e, n, i, j):
    if i <= s <= e <= j:
        return seg[n]
    if (e < i) | (s > j):
        return 0
    return find(s, (s + e) // 2, n * 2, i, j) + find((s + e) // 2 + 1, e, n * 2 + 1, i, j)

# 쿼리 수행
for Q in range(q):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        modify(1, n, 1, b, c)
    else:
        print(find(1, n, 1, b, c))