# 입력후 시간 계산식에 따라 계산, 출력
h, m, s = map(int, input().split())
deltatime = int(input())
s += deltatime 
m += s // 60
s %= 60
h += m // 60
m %= 60
h %= 24
print(h, m, s)