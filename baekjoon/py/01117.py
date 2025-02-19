# 입력
w, h, f, c, x1, y1, x2, y2 = map(int, input().split())

# 기본 사각형 넓이 추가
ans = (x2 - x1) * (y2 - y1)

# 만약 왼쪽 사각형이 오른쪽 사각형을 덮는다면 대칭
if f > w // 2:
    f = w - f

# 왼쪽사각형과 페인트가 겹치는 만큼을 한번 더 추가
if f > x1:
    ans += (min(f, x2) - x1) * (y2 - y1)

# 추가된 값에 c + 1만큼 곱
ans *= c + 1

# 전체 넓이에서 ans를 뺀 값을 출력
print(w * h - ans)