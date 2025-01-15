# 라이브러리 세팅
import sys

# 코드
for T in range(int(sys.stdin.readline())):                  # 테스트 케이스 입력
    start, time = map(int, sys.stdin.readline().split())    # 시작인구와 시간 입력
    print(start - time // 7 + time // 4)                    # 계산 결과를 출력