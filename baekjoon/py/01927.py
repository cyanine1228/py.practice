# 라이브러리 세팅
import sys

# 힙 선언
hip = [-1]

# 힙 추가 함수
def hip_add(n):
    hip.append(n)
    hip_up(len(hip) - 1)

# 힙 추가시 추가된 힙을 위로 올리는 함수
def hip_up(index):
    if hip[index] < hip[index // 2]:
        hip[index], hip[index // 2] = hip[index // 2], hip[index]
        hip_up(index // 2)

# 힙 제거 함수
def hip_remove():
    k = hip[1]
    if len(hip) == 2:
        hip.pop()
    else:
        hip[1] = hip.pop()
        hip_down(1)
    return k

# 힙 제거시 올라온 마지막 힙을 조건에 따라 다시 내리는 함수
def hip_down(index):
    after_index = -1
    if index * 2 + 1 >= len(hip):
        if index * 2 >= len(hip):
            return
        else:
            after_index = index * 2
    elif hip[index * 2] <= hip[index * 2 + 1]:
        after_index = index * 2
    else:
        after_index = index * 2 + 1
    if hip[index] > hip[after_index]:
        hip[index], hip[after_index] = hip[after_index], hip[index]
        hip_down(after_index)

# 실제 실행
for _ in range(int(sys.stdin.readline())):
    com = int(sys.stdin.readline())
    if com == 0:
        if len(hip) == 1:
            print(0)
        else:
            print(hip_remove())
    else:
        hip_add(com)