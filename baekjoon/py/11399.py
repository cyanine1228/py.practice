import sys                                           # 빠른 입출력을 위한 sys 라이브러리
n = int(sys.stdin.readline())                        # 사람 수
p = list(map(int, sys.stdin.readline().split()))     # 각 사람당 소요시간을 저장하는 리스트
p.sort()                                             # 리스트 정렬 : 첫번째 사람은 총합에서 n번 호출, 두번째사람은 n - 1번 호출... 이므로 정렬한 순서가 최소값
sum = 0                                              # 총합(정답) 선언
for i in range(n):                                   # 모든 p의값을 돌때까지 반복
    sum += p[i] * (n - i)                            # i번쨰사람은 p[i]만큼 소요하고 i번째와 그 이후의 모든 사람에게서 호출되므로 * (n + 1) 
print(sum)                                           # 총합 출력