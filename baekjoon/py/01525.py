# 라이브러리 세팅
from collections import deque

# 변수 세팅
lis = []
for i in range(3):
    lis = lis + list(map(int, input().split()))
lis = int("".join(map(str, lis)))
vi = set()
vi.add(lis)
ans = 123456780
que = deque([lis])
sum = 0

# 함수 세팅
def change(i, j):                       # i번째와 j번째를 교체한 리스트를 반환하는 함수
    lis2 = list(lis)
    lis2[i] = lis[j]
    lis2[j] = lis[i]
    return lis2

def ad(i, j):                           # 위의 change 함수를 이용해서 i번째와 j번째를 교환한 경우의수를 판단하는 함수
    k = "".join(map(str, change(i, j)))
    if not(int(k) in vi):
        que.append(int(k))
        vi.add(int(k))

# 실제 실행
while len(que) != 0:
    # 완성에 성공했으면 횟수 출력후 탈출
    if ans in vi:
        print(sum)
        exit(0)
    
    # 경우의 수가 많지 않기에 식 없이 노가다로 코드를 짰음음
    for i in range(len(que)):
        lis = que.popleft()
        lis = list(map(int, list(str(lis))))
        if len(lis) == 8:
            lis.insert(0, 0)
        l = lis.index(0)
        if l == 0:
            ad(0, 1)
            ad(0, 3)
        elif l == 1:
            ad(0, 1)
            ad(1, 2)
            ad(1, 4)
        elif l == 2:
            ad(1, 2)
            ad(5, 2)
        elif l == 3:
            ad(0, 3)
            ad(3, 4)
            ad(3, 6)
        elif l == 4:
            ad(4, 1)
            ad(4, 3)
            ad(4, 5)
            ad(4, 7)
        elif l == 5:
            ad(5, 2)
            ad(5, 4)
            ad(5, 8)
        elif l == 6:
            ad(6, 3)
            ad(6, 7)
        elif l == 7:
            ad(7, 4)
            ad(7, 6)
            ad(7, 8)
        else:
            ad(8, 5)
            ad(8, 7)
    sum += 1

# 모든 경우의수를 다해봤으나 답이 없을경우
else:
    print(-1)