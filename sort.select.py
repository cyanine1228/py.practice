def comp(a, b):                                # 두 값 비교
    if a > b:
        return True
    else:
        return False

def sort(lis):
    l = len(lis)
    for i in range(l):
        mi = lis[i]
        minum = i
        for j in range(i, l):
            if comp(mi, lis[j]):
                mi = lis[j]
                minum = j
        t = lis[i]
        lis[i] = lis[minum]
        lis[minum] = t
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

