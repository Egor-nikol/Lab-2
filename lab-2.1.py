sum_len_name = 0
name_author = input("Введите автора книги: ")
book_vector = []
m = []
with open("books.csv") as f:
    f.readline()
    i = 0
    for j in f.readlines():
        m.append(list(j.split(";")))
        if (len(m[i][1]) > 30):
            sum_len_name += 1
        if (m[i][3] == name_author):
            book_vector.append(m[i][1])
        i += 1
for i in book_vector:
    print(i, end="; ")
print(sum_len_name)


with open("ans.txt", "w") as f:
    vec = []
    count = 0
    for i in range(0, len(m), 4):
        count += 1
        print(str(count) + ".", m[i][3] + ".", m[i][1] + " -", m[i][6][6:10], file = f)
        if (count == 20):
            break

