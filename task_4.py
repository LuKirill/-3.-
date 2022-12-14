"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
from hashlib import sha512

cache_obj = {}


def url_(url):
    salt = "salt"
    if cache_obj.get(url):
        print(f'Url: {url} присутствует в кэше')
    else:
        res = sha512(url.encode() + salt.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


url_("https://gb.ru/lessons/260943")
url_("https://gb.ru/lessons/260943/homework")
url_("https://gb.ru/lessons/260943")
