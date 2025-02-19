# n 입력
n = int(input())

# 기본 그런디수 입력
grundy = [0, 1, 1, 1, 2, 2]

# mex함수
def mex(a):
    i = 0
    while i in a:
        i += 1
    return i

# 6번째부터 n번째까지의 그런디수 탐색
for i in range(6, n + 1):
    a = []
    a.append(grundy[i - 3])
    a.append(grundy[i - 4])
    for j in range(i - 4):
        k = i - 5 - j
        a.append(grundy[j] ^ grundy[k])
    grundy.append(mex(a))

# 그런디수 출력
if grundy[n] == 0:
    print(2)
else:
    print(1)