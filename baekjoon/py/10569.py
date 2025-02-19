# 테스트 케이스 수 입력
for i in range(int(input())):
    
    # 입, 출력
    v, e = map(int, input().split())
    print(e - v + 2)