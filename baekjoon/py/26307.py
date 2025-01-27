# 시, 분 입력후 조건에따라 출력
hour, minute = map(int, input().split())
print((hour - 9) * 60 + minute)