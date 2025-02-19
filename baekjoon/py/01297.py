# 라이브러리 세팅
import math

# 입력
d, h, w = map(int, input().split())

# 기본상태에서의 대각선 길이 저장
line = (h ** 2) + (w ** 2)

# 비율 저장
pro = math.sqrt(d ** 2 / line)

# 비율을 이용하여 답 출력
print(math.floor(h * pro), math.floor(w * pro))