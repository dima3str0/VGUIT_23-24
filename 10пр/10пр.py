from random import *

n = 4
a = list()

for i in range(n):
    b = []
    for j in range(n):
        b.append(randint(1,9))
    a.append(b)

with open('C:/Users/USER/Documents/GitHub/Dmitrys_Repository/10пр/Лаврентьев Дмитрий Вячеславович_УБ-31_vvod.txt','w') as file_vvod:
    for i in a:
        for j in i:
            file_vvod.write(str(j))
            file_vvod.write(' ')
        file_vvod.write('\n')
    file_vvod.close()

modify_a = list()

with open('C:/Users/USER/Documents/GitHub/Dmitrys_Repository/10пр/Лаврентьев Дмитрий Вячеславович_УБ-31_vvod.txt','r') as file_vvod:
    for i in file_vvod:
        i = i.replace(' ','')
        modify_a.append(i[:-1])
    file_vvod.close()

modify_a_best = list()

for i in modify_a:
    b = list()
    for j in i:
        j = int(j)
        b.append(j)
    modify_a_best.append(b)

for i in modify_a_best:
    i[i.index(max(i))],i[0] = i[0],i[i.index(max(i))]
    i[i.index(min(i))],i[-1] = i[-1],i[i.index(min(i))]

with open('C:/Users/USER/Documents/GitHub/Dmitrys_Repository/10пр/Лаврентьев Дмитрий Вячеславович_УБ-31_vivod.txt','w') as file_vivod:
    for i in modify_a_best:
        for j in i:
            file_vivod.write(str(j))
            file_vivod.write(' ')
        file_vivod.write('\n')
    file_vivod.close()
