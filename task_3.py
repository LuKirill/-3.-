"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

from hashlib import sha256


def string_rush():
    my_str = str(input())
    my_str_copy = my_str[::-1]
    my_set = set()
    n = len(my_str)
    while n > 0:
        a = [my_str[i:i+n-1] for i in range(0, len(my_str), n)]
        for i in a:
            my_set.add(sha256((i.encode())).hexdigest())
        n -= 1
        if n == 0:
            break
    m = len(my_str_copy)
    while m > 0:
        b = [my_str_copy[j:j+m-1] for j in range(0, len(my_str_copy), m)]
        for j in b:
            my_set.add(sha256((j.encode())).hexdigest())
        m -= 1
        if m == 0:
            break
    return list(my_set)


print(string_rush())
