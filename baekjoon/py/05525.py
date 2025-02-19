# 라이브러리 세팅
import sys

# 변수 세팅
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())
ans = 0
stack = []
res = []
past = "O"

# 문자열을 Pn들로 분할
for i in s:
    if i != past:
        stack.append(i)
    else:
        if i == "O":
            if len(stack) != 0:
                stack.pop()
                res.append(list(stack))
            stack = []
        else:
            res.append(list(stack))
            stack = [i]
    past = i
if len(stack) != 0:
    if stack[len(stack) - 1] == "O":
        stack.pop()
    res.append(stack)

# 분할된 문자열을 이용하여 답 탐색
ans = 0
for i in res:
    k = len(i) // 2 + 1
    if k - n > 0:
        ans += k - n
print(ans)