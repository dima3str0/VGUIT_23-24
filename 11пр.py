from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext

def button_number(name):
    return Button(tab_calculator,text=name,command=lambda:add_number(name))

def button_operation(name):
    return Button(tab_calculator,text=name,command=lambda:add_operation(name))

def add_number(number):
    value = bar.get() + str(number)
    bar.delete(0,END)
    bar.insert(0,value)

def add_operation(operation):
    value = bar.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    bar.delete(0,END)
    bar.insert(0,value+operation)

def calculation():
    value = bar.get()
    bar.delete(0,END)
    bar.insert(0,eval(value))

def clear():
    bar.delete(0,END)

def checkbox(name,value):
    return Radiobutton(tab_checkbox,text=name,value=value,variable=selected)

def using_button():
    active_button = 'Вы выбрали вариант под номером' + ' ' + str(selected.get()) + '!'
    messagebox.showinfo(title='Ваш выбор',message=active_button)

def open_file():
    file_selected = filedialog.askopenfilename(defaultextension='txt')
    if file_selected != '':
        with open(file_selected,'r') as file:
            text = file.read()
            text_file.delete("1.0", END)
            text_file.insert("1.0", text)
            file.close()

#Создаём окно
win = Tk()
win.title('Лаврентьев Дмитрий Вяеславович')
win.geometry('337x301+250+100')
win.resizable(False,False)

#Создаём вкладки
tab_control = ttk.Notebook(win)

tab_calculator = ttk.Frame(tab_control)
tab_control.add(tab_calculator,text='Калькулятор')

tab_checkbox = ttk.Frame(tab_control)
tab_control.add(tab_checkbox,text='Чекбокс')

tab_text = ttk.Frame(tab_control)
tab_control.add(tab_text,text='Текст')
tab_text.rowconfigure(0,weight=1)

#Калькулятор
bar = Entry(tab_calculator,justify=RIGHT,font=('Airal',20))
bar.grid(row=0,column=0,columnspan=5,padx=14,stick='wens')

button_number('1').grid(row=4,column=0,stick='wens')
button_number('2').grid(row=4,column=1,stick='wens')
button_number('3').grid(row=4,column=2,stick='wens')
button_number('4').grid(row=3,column=0,stick='wens')
button_number('5').grid(row=3,column=1,stick='wens')
button_number('6').grid(row=3,column=2,stick='wens')
button_number('7').grid(row=2,column=0,stick='wens')
button_number('8').grid(row=2,column=1,stick='wens')
button_number('9').grid(row=2,column=2,stick='wens')
button_number('0').grid(row=5,column=0,stick='wens',columnspan=2)

button_operation('*').grid(row=3,column=3,stick='wens')
button_operation('/').grid(row=2,column=3,stick='wens')
button_operation('+').grid(row=5,column=3,stick='wens')
button_operation('-').grid(row=4,column=3,stick='wens')

Button(tab_calculator,text='Clear',command=lambda:clear()).grid(row=2,column=4,stick='wens',rowspan=4)

Button(tab_calculator,text='=',command=lambda:calculation()).grid(row=5,column=2,stick='wens')

tab_calculator.grid_columnconfigure(0,minsize=60)
tab_calculator.grid_columnconfigure(1,minsize=60)
tab_calculator.grid_columnconfigure(2,minsize=60)
tab_calculator.grid_columnconfigure(3,minsize=60)

tab_calculator.grid_rowconfigure(2,minsize=60)
tab_calculator.grid_rowconfigure(3,minsize=60)
tab_calculator.grid_rowconfigure(4,minsize=60)
tab_calculator.grid_rowconfigure(5,minsize=60)

#Чекбоксы
selected = IntVar()

checkbox('Первый',1).grid(row=0,column=0,padx=23)
checkbox('Второй',2).grid(row=0,column=1,padx=23)
checkbox('Третий',3).grid(row=0,column=2,padx=23)

Button(tab_checkbox,text='Кнопка',command=lambda:using_button()).grid(row=2,column=0,columnspan=3,stick='wens')

#Текст
text_file = Text(tab_text,wrap=WORD,width=38)
text_file.grid(column=0,row=0,sticky='wens')

menu = Menu(win)
new_item = Menu(menu)
new_item.add_command(label='Загрузить файл',command=lambda:open_file())
menu.add_cascade(label='Файл', menu=new_item)

scroll=ttk.Scrollbar(tab_text,orient=VERTICAL,command=text_file.yview)
scroll.grid(column=1,row=0,stick=NS)
text_file['yscrollcommand'] = scroll.set

#Распаковка
tab_control.pack(side=LEFT)
first_state = BooleanVar()
second_state = BooleanVar()
thrid_state = BooleanVar()
win.config(menu=menu)
win.mainloop()
