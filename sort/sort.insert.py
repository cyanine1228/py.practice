def comp(a, b):                                # 앞 뒤 값 비교
    if a > b:
        return False
    else:
        return True
    
def sort(lis):
    l = len(lis)
    for i in range(1, l):
        j = i - 1
        while comp(lis[i], lis[j]):
            j -= 1
            if j == -1:
                break
        j += 1
        lis.insert(j, lis.pop(i))
    return lis

a = [3, 5, 4, 6, 1]
a = sort(a)
b = [2, 1, 6, 123, 4, 6, 2, 5, 120, 234567, 1, 564, 2]
b = sort(b)
c = [2, 1]
c = sort(c)
print(a)
print(b)
print(c)