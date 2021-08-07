# проверка таблицы умножения
import random
import time
import colorama
from termcolor import cprint

def rnd2():
    x, y = map(int, (random.uniform(3, 10), random.uniform(4, 10)))
    return x, y, x * y

colorama.init()
err = 0
mtable = []
a, b, mtmp = rnd2()
for i in range(10):
    while mtmp in mtable:
        a, b, mtmp = rnd2()
    print(a, '*', b, '= ', end=' ')
    mtable.append(mtmp)
    number = input("")
    if not number.isdecimal():
        res = 0
    else:
        res = int(number)
    if res == mtmp:
        cprint("Правильно", 'cyan')
    else:
        cprint("Неправильно", 'red')
        err += 1
if err > 2:
    cprint("Больше 2х ошибок - плохо, учи еще !!!", 'red')
elif err > 1:
    cprint("Две ошибки - можно и лучше, не мешает подучить.", 'yellow')
elif err > 0:
    cprint("Одна ошибка - неплохо.", 'yellow')
else:
    cprint("Ошибок нет - Молодец, так держать  !!!", 'cyan')

time.sleep(2)
number = input()
