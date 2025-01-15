n, m = map(int, input().split())            # 시작수, 목표수 입력
if n >= m:                                  # n이더 크거나 같다면 무조건 -1 반복이 제일 빠르므로 예외처리
    print(n - m)
    exit(0)
lis = [n]                                   # 현재 경우의수가 n하나이므로 경우의수에 n추가
sum = 0                                     # 이동 횟수 선언
vi = {n}
maxsum = 100000000000000000
while not(m in lis):                        # m이 경우에 수에 포함될때 까지 반복
    lis2 = []                               # 다음 경우의수를 저장할 리스트 선언
    for i in range(len(lis)):               # 다음 경우의수에 +1 -1 *2 추가
        if (not(lis[i] + 1 in vi)) & (lis[i] != 100000):
            lis2.append(lis[i] + 1)
            vi.add(lis[i] + 1)
        if (not(lis[i] - 1 in vi)) & (lis[i] != 0):
            lis2.append(lis[i] - 1)
            vi.add(lis[i] - 1)
        if lis[i] <= 50000:
            if (lis[i] * 2 >= m) & (maxsum > lis[i] * 2 - m + sum + 1):   # 만약에 *2가 m을 초과한다면
                maxsum = lis[i] * 2 - m + sum + 1                       # 역대 m을 넘었던 수중 가장 횟수가 작은수를 저장
            elif not(lis[i] * 2 in vi):
                lis2.append(lis[i] * 2)
                vi.add(lis[i] * 2)
    sum += 1                                # 이동횟수 추가
    lis = list(set(lis2))                   # 현재 경우의수를 다음 경우의수로 변환
print(min(sum, maxsum))                     # 이동횟수 출력