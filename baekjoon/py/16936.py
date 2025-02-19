# 라이브러리 세팅
import sys

# n 입력
n = int(sys.stdin.readline())

# 특정값 k를 소인수 분해했을때 2의 지수를 반환
def two(k):
    two = 0
    while k % 2 == 0:
        k //= 2
        two += 1
    return two

# 특정값 k를 소인수 분해했을때 3의 지수를 반환
def three(k):
    three = 0
    while k % 3 == 0:
        k //= 3
        three += 1
    return three

# b 입력
b = list(map(int, sys.stdin.readline().split()))

# b에서 원소의 3의지수가 줄어들고 2의 지수가 오르는 순으로 정렬
# 반드시 3의 지수는 점점줄고, 2의지수는 점점 오르므로
b.sort(key = lambda x:(-three(x), two(x)))

# 출력
print(*b)