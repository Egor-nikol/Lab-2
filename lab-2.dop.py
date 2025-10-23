import csv
from io import StringIO


def comp(a):
    return a[-2]

m = []
s = set()
i = 0
with open("books-en.csv") as f:
    f.readline()
    for j in f.readlines():
        
        m.append(list(csv.reader(StringIO(j), delimiter=';', quotechar='"'))[0])
        s.add(m[i][-3])
        i += 1

for i in sorted(s):
    print(i, end = " ")
 
print()
print("_" * 110)
print()

m.sort(key=comp, reverse=True)
for i in range(20):
    print(m[i][1])
