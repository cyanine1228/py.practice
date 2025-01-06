import time
import random
starttime = time.time()
def sort(lis):
    res = []
    l = len(lis)
    res.append(lis)
    while len(res) != l:
        for it in range(len(res)):
            i = list()
            i = res[it]
            if len(i) != 1:
                front = []
                end = []
                pivot = i.pop(len(i) // 2)
                end = i
                k = 0
                for j in range(len(end)):
                    if end[j - k] <= pivot:
                        front.append(end.pop(j - k))
                        k += 1
                res.pop(it)
                if len(end) > 0:
                    res.insert(it, end)
                res.insert(it, [pivot])
                if len(front) > 0:
                    res.insert(it, front)
    result = list()
    for i in res:
        result.append(i[0])
    return result

a = [3, 5, 4, 6, 1]
a = sort(a)
b = [2, 1, 6, 123, 4, 6, 2, 5, 120, 234567, 1, 564, 2]
b = sort(b)
c = [2, 1]
c = sort(c)
d = list()
for i in range(1000):
    d.append(random.randrange(1, 1001))
d = sort(d)
print(a)
print(b)
print(c)
print(d)
endtime = time.time()
print(endtime - starttime)

