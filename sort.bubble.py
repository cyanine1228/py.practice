def comp(a, b):                                # 앞 뒤 값 비교
    if a > b:
        return True
    else:
        return False

def sort(lis):                                   # 버블소트
    l = len(lis)                                 # 길이 저장
    for i in range(l - 1):                       # 반복횟수 지정
        for j in range(1, l - i):                # 반복 횟수당 비교 시행 위치 설정
            if comp(lis[j - 1], lis[j]):         # 두 값 비교후 앞 값이 더 크다면
                t = lis[j - 1]                   # 임시 변수 t에 앞 값 저장
                lis[j - 1] = lis[j]              # 앞 값을 뒷 값으로 변경
                lis[j] = t                       # 뒷 값을 t(기존 앞 값)으로 변경
    return lis                                   # 정렬된 리스트를 반환
a = [3, 5, 4, 6, 1]
a = sort(a)
b = [2, 1, 6, 123, 4, 6, 2, 5, 120, 234567, 1, 564, 2]
b = sort(b)
c = [2, 1]
c = sort(c)
print(a)
print(b)
print(c)






