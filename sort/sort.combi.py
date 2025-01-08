import time
import random
starttime = time.time()  

def sort(lis):
    if len(lis) <= 1:
        return lis
    n = len(lis) // 2
    lis1 = sort(lis[:n])
    lis2 = sort(lis[n:])
    i = 0
    j = 0
    lis3 = []
    while (len(lis1) != 0) & (len(lis2) != 0):
        if(lis1[0] < lis2[0]):
            lis3.append(lis1.pop(0))
        else:
            lis3.append(lis2.pop(0))
    if len(lis1) == 0:
        while(len(lis2) != 0):
            lis3.append(lis2.pop(0))
    else:
        while(len(lis1) != 0):
            lis3.append(lis1.pop(0))
    return lis3

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