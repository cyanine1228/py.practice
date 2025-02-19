# 답을 저장할 배열
s = []

# 번호를 저장할 변수
ans = int(input())

# 현재 탐색중인 번호를 저장할 변수
sum = 0

# n자리 감소하는 수를 찾고 sum에 1을 더한후 ans와 동일하다면 출력하는 함수
def find(n):
    global sum
    if n == 0:
        sum += 1
        if ans == sum:
            print("".join(list(map(str, s))))
            exit(0)
    for i in range(10):
        s.append(i)
        infind(i, n - 1)
        s.pop()

# find의 내부함수
def infind(l, n):
    global sum
    if n == 0:
        sum += 1
        if ans == sum:
            print("".join(list(map(str, s))))
            exit(0)
    for i in range(l):
        s.append(i)
        infind(i, n - 1)
        s.pop()

# 1자리수부터 10자리수까지 탐색후 11자리가 된다면 -1출력, 탈추 
n = 1
while True:
    find(n)
    n += 1
    if n == 11:
        print(-1)
        break