# 라이브러리 세팅
import sys

# 변수 세팅
seg = []
ans = []
n = 0

# 세그먼트 변경함수(전 과정 포함)
def segmodify(i, p):
    if p > 0:
        p = 1
    elif p < 0:
        p = -1
    segmodify2(1, n, 1, i, p)

# 세그먼트 변경함수(각 과정)
def segmodify2(s, e, n, i, p):
    if s == e:
        if s == i:
            seg[n] = p
            return
        else:
            return
    if s <= i <= e:
        segmodify2(s, (s + e) // 2, n * 2, i, p)
        segmodify2((s + e) // 2 + 1, e, n * 2 + 1, i, p)
        seg[n] = seg[n * 2] * seg[n * 2 + 1]
        return
    
# 세그먼트 곱함수(전 과정 포함)
def segsq(a, b):
    k = segsq2(1, n, 1, a, b)
    if k == 0:
        ans.append("0")
    elif k > 0:
        ans.append("+")
    else:
        ans.append("-")

# 세그먼트 곱함수(각 과정)
def segsq2(s, e, n, a, b):
    if a <= s <= e <= b:
        return seg[n]
    if (s > b) | (e < a):
        return 1
    return segsq2(s, (s + e) // 2, n * 2, a, b) * segsq2((s + e) // 2 + 1, e, n * 2 + 1, a, b)

# 무한 반복
while True:

    # 입력이 남아있다면
    try:

        # 변수 초기화, 세그먼트트리 세팅
        ans = []
        n, k = map(int, sys.stdin.readline().split())
        seg = [0] * (n * 4)
        x = list(map(int, sys.stdin.readline().split()))
        for i in range(n):
            segmodify(i + 1, x[i])
            
        # 명령 수행
        for i in range(k):
            d, a, b = sys.stdin.readline().split()
            a = int(a)
            b = int(b)
            if d == "C":
                segmodify(a, b)
            else:
                segsq(a, b)

        # 답 출력
        print("".join(ans))

    # 입력이 끝났다면 탈출
    except:
        break