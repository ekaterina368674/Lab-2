import csv


def esc(code):
    return f'\u001b[{code}m'


GREEN = esc(42)
END = esc(0)
YELLOW = esc(43)
RED = esc(41)
WHITE = esc(47)
count_less_150 = 0
count_more_150 = 0
N = int(input("Сколько раз повторить рисунок?"))

n = 3
count = 0
k = 0


def Flag():  # Создание флага
    for i in range(3):
        print(WHITE + ' ' * 20 + END)
    for i in range(3):
        print(RED + ' ' * 20 + END)


def Pattern(N):  # Создание рисунка нужное количество раз вниз и вправо
    for i in range(N):
        count1 = 1
        count0 = 2
        n = 2
        print((' ' * (26 - n) + '11' + ' ' * (49 - 2 * n) + '11' + ' '*(29-n))*N)
        count1 += 6
        n += 3
        count0 += 2
        for i in range(6):
            print((' ' * (26 - n) + '1' * (count1 - count0) + ' ' * 2 * (count0 - 3) + '1' * (
                    count1 - count0) + ' ' * (49 - 2 * n) + '1' * (count1 - count0) + ' ' * 2 * (count0 - 3) + '1' * (
                           count1 - count0) + ' '*(29-n))*N)
            count1 += 3
            count0 += 3
            n += 3

        print((' ' * (26 - n) + '1' * (count1 - count0) + ' ' * count0 + ' ' * (count0 - 6) + '1' * (
                count1 - count0) + ' ' * 3 + '1' * (count1 - count0) + ' ' * count0 + ' ' * (count0 - 6) + '1' * (
                       count1 - count0) + ' '*(29-n)) * N)
        print((' ' * (26 - n - 3) + '1' * (count1 - count0) + ' ' * 2 * count0 + '1' * (
                count1 - count0) + ' ' * (70 - n - 3) + '1' * (count1 - count0) + ' '*(29-n-3))*N)
        print((' ' * (26 - n) + '1' * (count1 - count0) + ' ' * count0 + ' ' * (count0 - 6) + '1' * (
                count1 - count0) + ' ' * 3 + '1' * (count1 - count0) + ' ' * count0 + ' ' * (count0 - 6) + '1' * (
                       count1 - count0) + ' '*(29-n)) * N)

        for i in range(6):
            print((' ' * (29 - n) + '1' * (count1 - count0) + ' ' * 2 * (count0 - 6) + '1' * (
                    count1 - count0) + ' ' * (55 - 2 * n) + '1' * (count1 - count0) + ' ' * 2 * (count0 - 6) + '1' * (
                           count1 - count0) + ' '*(32-n))*N)
            count1 -= 3
            count0 -= 3
            n -= 3
        print((' ' * (29 - n) + '11' + ' ' * (55 - 2 * n) + '11' + ' '*(32-n))*N)
        print()


def Function():  # Создание графика функции
    x = [i for i in range(0, 101) if i ** 0.5 % 1 == 0]
    for i in range(len(x) - 2, -1, -1):
        print(int(x[i] ** 0.5), ' ' * x[i] + RED + '\\' * (x[i + 1] - x[i]) + END)
    print(end=' ')
    s = [str(i) for i in range(101)]
    print(''.join(s[:10]), end='')
    s1 = [str(int(i) // 10) for i in s[10:]]
    print(''.join(s1))
    s2 = [str(int(i) % 10) for i in s[10:]]
    print(' ' * 12 + ''.join(s2))
    print()


def Diagram():  # Функция для вывода диаграммы
    a = 'Книги после 2017 года '
    b = 'Книги до 2017 года '
    c = len(a) + 31 + 3
    print(WHITE + ' ' * c + END)
    print(
        WHITE + b + WHITE + ' ' * (len(a) - len(b)) + RED + '   ' * p1 + WHITE + ' ' * (c - len(b + '   ' * p1)) + END)
    print(WHITE + ' ' * c + END)
    print(WHITE + a + RED + '   ' * p2 + WHITE + ' ' * (c - len(a + '   ' * p2)) + END)
    print(WHITE + ' ' * c + END)
    print(WHITE + ' ' * (len(a) - 1) + END + WHITE + '0 10 20 30 40 50 60 70 80 90 100  %' + END)


def Diagram_en():  # Функция для вывода диаграммы (Для books-en)
    a = 'Книги после 2000 года '
    b = 'Книги до 2000 года '
    c = len(a) + 31 + 3
    print(WHITE + ' ' * c + END)
    print(
        WHITE + b + WHITE + ' ' * (len(a) - len(b)) + RED + '   ' * p1 + WHITE + ' ' * (c - len(a + '   ' * p1)) + END)
    print(WHITE + ' ' * c + END)
    print(WHITE + a + RED + '   ' * p2 + WHITE + ' ' * (c - len(a + '   ' * p2)) + END)
    print(WHITE + ' ' * c + END)
    print(WHITE + ' ' * (len(a) - 1) + END + WHITE + '0 10 20 30 40 50 60 70 80 90 100  %' + END)

print("Флаг Польши")
Flag()

print("\n" * 2 + "Рисунок")
Pattern(N)

print("\n" * 2 + "Функция у = х ^ 0,5")
Function()

print('\nДиаграмма для books.csv\n')
with open('books.csv', encoding='cp1251') as r_file:
    book_list = csv.DictReader(r_file, delimiter=';')
    for row in book_list:
        count += 1
        if int(row["Дата поступления"][:4]) <= 2017:
            k += 1
p1 = round(int(round(k / count, 2) * 100), -1) // 10  # процент книг до 2017
p2 = 10 - p1  # процент книг после 2017
Diagram()

count_en = 0
k_en = 0
print('\nДиаграмма для books-en.csv\n')
with open('books-en.csv', encoding='cp1251') as r_file:
    book_list = csv.DictReader(r_file, delimiter=';')
    for row in book_list:
        count_en += 1
        if len(row["Year-Of-Publication"]) == 4:
            if int(row["Year-Of-Publication"]) <= 2000:
                k_en += 1

p1 = round(int(round(k_en / count_en, 2) * 100), -1) // 10  # процент книг до 2000
p2 = 10 - p1  # процент книг после 2000
Diagram_en()