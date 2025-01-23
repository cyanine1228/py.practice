# 라이브러리 세팅
from collections import deque

# 기본 변수 세팅
capa = list(map(int, input().split()))
ans = {capa[2]}
water = [0, 0, capa[2]]
vi = {tuple(water)}
que = deque([water])

# 물 이동 함수 세팅(i에서 j로 부을때)
def watermove(i, j):
    water2 = list(water)
    if water2[i] <= capa[j] - water2[j]:
        water2[j] += water2[i]
        water2[i] = 0
    else:
        water2[i] -= capa[j] - water2[j]
        water2[j] = capa[j]
    if not(tuple(water2) in vi):
        vi.add(tuple(water2))
        que.append(water2)
        if water2[0] == 0:
            ans.add(water2[2])
        return
    
# 실제 실행
while len(que) != 0:
    water = que.popleft()
    watermove(0, 1)
    watermove(0, 2)
    watermove(1, 0)
    watermove(1, 2)
    watermove(2, 0)
    watermove(2, 1)

# 정답 정리후 출력
ans = list(ans)
ans.sort()
print(*ans)