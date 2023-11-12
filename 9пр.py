# Блок А Задание 1
x = int(input('Введите число: '))
n = int(input('Введите число: '))

def func(n):
    if n == 0:
        return 1
    return func(n-1)*n

print((x**n)/(func(n)))

# Блок Б Задание 3

def f():
    a = int(input('Введите число: '))
    if a == 0:
        exit()
    else:
        print(a)
        f_1()

def f_1():
    a = int(input('Введите число: '))
    if a == 0:
        exit()
    else:f()


f()
