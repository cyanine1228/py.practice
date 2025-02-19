# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
crain = list(map(int, sys.stdin.readline().split()))
crain.sort()
m = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
crain.sort(reverse=True)
box.sort()

# 예외처리(불가능한 경우)
if box[len(box) - 1] > crain[0]:
    print(-1)
    exit(0)

# 모든 박스가 사라질때까지 반복
t = 0
while len(box) != 0:

    # 시간 경과
    t += 1

    # 최대중량이 높은 크레인들부터 자신이 가져갈 수 있는 최대무게의 박스를 제거
    for k in crain:
        i = len(box) - 1
        while i >= 0:
            if k >= box[i]:
                box.pop(i)
                break
            i -= 1

# 시간 출력
print(t)