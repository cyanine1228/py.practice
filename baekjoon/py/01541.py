# 라이브러리 세팅
import sys

# 변수 세팅
line = list(sys.stdin.readline().strip())
ans = 0
now = ""
sum = 0
minus = 0

# 시행
for i in range(len(line)):
    if line[i] == "-":
        sum += int(now)
        if minus == 0:
            minus = 1
            ans += sum
        else:
            ans -= sum
        sum = 0
        now = ""

    elif line[i] == "+":
        sum += int(now)
        now = ""
    else:
        now += line[i]
if minus == 0:
    sum += int(now)
    ans += sum
else:
    sum += int(now)
    ans -= sum

# 출력
print(ans)