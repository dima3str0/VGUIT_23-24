import requests
import json
from tkinter import *

def using_button():
    name_repository = str(bar_text_vvod.get())
    url = f"https://api.github.com/users/{name_repository}"
    response = requests.get(url).json()

    keys = ['company','created_at','email','id','name','url']
    response_modified = {}
    for element in keys:
        response_modified[element] = response[element]

    with open('site_information.txt','w') as file:
        json.dump(response_modified,file,indent=3)


win = Tk()
win.configure(background='azure3')
win.title('Информация о репозитории')
win.geometry('500x400+500+100')

title = Label(win,text='Введите название репозитория',width=30,height=1,font=('Arial 20 bold'),bg='azure3').grid(row=0)
bar_text_vvod = Entry(win,width=35,borderwidth=5)
bar_text_vvod.grid(row=1)
bar_text_vvod.focus()
button = Button(win,text='Получить информацию',width=30,height=2,command=lambda :using_button()).grid(row=2,pady=20)


win.mainloop()
