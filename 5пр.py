# Вариант 1
s = str(input('Введите текст на русском языке: '))
k = 0
if (s[0] == 'е') or (s[0] == 'Е'):
        k += 1
for i in range(len(s)-1):
    if (s[i] == ' ') and ((s[i+1] == 'е') or (s[i+1] == 'Е')):
        k += 1
print(k)

# Вариант 2
s = str(input(''))
s = s.replace(':','%')
print(s.count('%'))
print(s)

# Вариант 3
s = str(input(''))
print(s.count('.'))
s = s.replace('.','')
print(s)

# Вариант 4
s = str(input(''))
s = s.replace('а','о')
print(s,len(s))

# Вариант 5
s = str(input(''))
s = s.upper()
print(s)

# Вариант 6
s = str(input(''))
s = s.lower()
print(s.count('а'))
s = s.replace('а','')
print(s)

# Вариант 7
s = str(input(''))
s = s.replace('п','*',(s.count('п',0,(len(s)//2))))
print(s)

# Вариант 8
s = str(input(''))
print((s.count(' '))+1)

# Вариант 9
s = str(input('Текст: '))
m = str(input('Слово: '))
print(s.count(m))

# Вариант 10
s = str(input('Текст на английском: '))
h = ''
s = s.replace(s[0],s[0].upper(),1)
for i in range(len(s)):
    if s[i-1] == ' ':
        h += s[i].upper()
    else:h += s[i]
print(h)
