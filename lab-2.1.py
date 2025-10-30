import random


sum_len_name = 0
name_author = input("Введите автора книги: ")
book_vector = []
mas_books = []
name_book = 1
autor_book = 3
with open("books.csv") as f:
    f.readline()
    for line in f: 
        line = list(line.split(";"))
        mas_books.append(line)
        if (len(line[name_book]) > 30):
            sum_len_name += 1
        if (name_author == line[autor_book]):
            book_vector.append(line[name_book]) 
print(sum_len_name)
print()
for el in book_vector:
    print(el, end="; ")


with open("ans.txt", "w") as f:
    count = 0
    random_strings = random.sample(mas_books, 20)
    for string in random_strings:
        count += 1
        print(str(count) + ".", string[autor_book] + ".", string[name_book] + 
              " -", string[6][6:10], file = f)


