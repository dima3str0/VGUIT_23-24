from random import *
from math import *

#Вариант 1 Задание 1

def square(figure):

    if figure == 'Квадрат':
        a = int(input('Введите длину: '))
        print('Площадь квадрата:',a**2)

    elif figure == 'Прямоугольник':
        a = int(input('Введите длину: '))
        b = int(input('Введите ширину: '))
        print('Площадь прямоугольника:', (a+b)*2)

    elif figure == 'Круг':
        a = int(input('Введите радиус: '))
        print('Площадь круга:', 3.14 * (a**2))

    elif figure == 'Ромб':
        a = int(input('Введите длину первой диагонали: '))
        b = int(input('Введите длину второй диагонали: '))
        print('Площадь ромба:',(a+b)/2)

square(str(input('Введите название фигуры: ')))

#Вариант 1 Задание 2

m = [randint(1,100) for i in range(15)]
n = [randint(1,100) for i in range(10)]
c = [randint(1,100) for i in range(5)]

cr_m = 0
cr_n = 0
cr_c = 0

for i in m:
    cr_m += i
print('Сумма элементов первого массива равна:',cr_m)
cr_m /= len(m)
print('Среднее арифметическое первого массива равно:',cr_m,'\n')

for i in n:
    cr_n += i
print('Сумма элементов второго массива равна:',cr_n)
cr_n /= len(n)
print('Среднее арифметическое второго массива равно:',cr_n,'\n')

for i in c:
    cr_c += i
print('Сумма элементов третьего массива равна:',cr_c)
cr_c /= len(c)
print('Среднее арифметическое третьего массива равно:',cr_c,'\n')

# Вариант 2 Задание 1

h = int(input('Введите высоту треугольника: ',))
a = int(input('Введите длину стороны, на которую опущена высота треугольника: '))

print('Площадь шестиугольника равна: ',(1/2*a*h)*6)

# Вариант 2 Задание 2

def square1(a,b):
    print('Площадь треугольника:',(a+b)*2)

square1(5,10)
square1(10,15)
square1(15,20)


# Вариант 3 Задание 1

def hypotenuse(a,b):
    return sqrt(a**2 + b**2)

if hypotenuse(5,10) > hypotenuse(10,15):
    print('Первая гипотенуза больше')
else:
    print('Первая гипотенуза меньше')

# Вариант 3 Задание 2

s = ['t','z','b','u','a']

s.sort()
print(s)

# Вариант 4 Задание 1

def f(c,d):
    while NOD(c,d) != 1:
        nod = NOD(c,d)
        c /= nod
        d /= nod
        if NOD(c,d) == 1:
            print('Ответ: ',int(c),'/',int(d))
            break


def NOD(a,b):

    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return (a+b)

f(int(input('Числитель ')),int(input('Знаменатель ')))
