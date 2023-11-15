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
    n = int(input('Введите длину строки: '))
    for i in range(n):
        a = int(input('Введите число: '))
        if (i+1) % 2 != 0:
            print(a)
        if a == 0:
            break

f()
