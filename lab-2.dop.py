import csv


publisher = -3
Book_Title = 1
mas_id = []
s = set()
i = 0
with open("books-en.csv") as f:
    f.readline()
    for j in f.readlines():
        mas_id.append(list(csv.reader([j], delimiter=';', quotechar='"'))[0])
        s.add(mas_id[i][publisher])
        i += 1

for el in sorted(s):
    print(el, end=" ")
 
print()
print("_" * 110)
print()

mas_id.sort(key=lambda el: el[-2], reverse=True)
for i in range(20):
    print(mas_id[i][Book_Title])
