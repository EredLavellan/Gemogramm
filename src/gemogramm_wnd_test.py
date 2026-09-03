from tkinter import *
from src.example_1 import Gemogramm

def clicked():
    global sex
    global gemoglobin
    global eritrocit
    global reticul
    global tromb
    sex=txt_1.get()
    gemoglobin=txt_2.get()
    eritrocit=txt_3.get()
    reticul=txt_4.get()
    tromb=txt_5.get()
    wnd.destroy()

wnd = Tk()
wnd.title("Gemoramm")
wnd.geometry("500x500")
wnd.resizable(False, False)
fnt_1=("Arial", 13, "bold") #Шрифт 1
fnt_2=("Arial", 13, "italic") #Шрифт 2
fnt_3=("Arial", 10, "bold") #Шрифт 3

sex=''
gemoglobin=''
eritrocit=''
reticul=''
tromb=''

lbl_1 = Label(master=wnd, text="Введите пол пациента: ")
lbl_1.configure(font=fnt_1)
lbl_1.place(x=10, y=20)
txt_1 = Entry(master=wnd, width=30)
txt_1.configure(font=fnt_2)
txt_1.place(x=10, y=50)

lbl_2 = Label(master=wnd, text="Введите показатель гемоглобина: ")
lbl_2.configure(font=fnt_1)
lbl_2.place(x=10, y=80)
txt_2 = Entry(master=wnd, width=30)
txt_2.configure(font=fnt_2)
txt_2.place(x=10, y=110)

lbl_3 = Label(master=wnd, text="Введите показатель эритроцитов: ")
lbl_3.configure(font=fnt_1)
lbl_3.place(x=10, y=140)
txt_3 = Entry(master=wnd, width=30)
txt_3.configure(font=fnt_2)
txt_3.place(x=10, y=170)

lbl_4 = Label(master=wnd, text="Введите показатель ретикулоцитов: ")
lbl_4.configure(font=fnt_1)
lbl_4.place(x=10, y=200)
txt_4 = Entry(master=wnd, width=30)
txt_4.configure(font=fnt_2)
txt_4.place(x=10, y=230)

lbl_5 = Label(master=wnd, text="Введите показатель тромбоцитов: ")
lbl_5.configure(font=fnt_1)
lbl_5.place(x=10, y=260)
txt_5 = Entry(master=wnd, width=30)
txt_5.configure(font=fnt_2)
txt_5.place(x=10, y=290)

btn_1 = Button(master=wnd, text="OK") #Создание объекта первой кнопки
btn_2=Button(master=wnd, text="Cancel") #Создание объекта второй кнопки
btn_1.configure(font=fnt_3) #Шрифт для первой кнопки
btn_1.configure(command=clicked) #Команда для первой кнопки
btn_2.configure(font=fnt_3) #Шрифт для второй кнопки
btn_2.configure(command=wnd.destroy) #Команда для второй кнопки - закрытие окна
btn_1.place(x=40, y=320, width=100, height=30) #размещение первой кнопки в окне
btn_2.place(x=150, y=320, width=100, height=30)

wnd.mainloop()

if sex!="" and gemoglobin!="" and eritrocit!="" and reticul!="" and tromb!="":
    msg = Tk()  # Создание объекта второго окна
    msg.title("Gemogramm")  # Заголовок окна
    msg.geometry("500x500")  # Геометрические размеры окна
    msg.resizable(False, False)

    result = Gemogramm(sex.title(), int(gemoglobin), float(eritrocit), float(reticul), int(tromb))

    lbl = Label(master=msg, text=f"Диагноз:\n{result.diagnose}",relief=GROOVE)  # Метка с сообщением для второго окна, relief - создает рамку

    lbl.configure(font=fnt_1)  # Шрифт для метки
    lbl.place(x=10, y=10, height=100, width=480)  # Размещение объекта кнопки
    btn = Button(master=msg, text="OK")  # Создание объекта кнопки
    btn.configure(font=fnt_3)  # Шрифт для кнопки
    btn.configure(command=msg.destroy)  # Метод для обработки нажатия кнопки
    btn.place(x=200, y=120, width=100, height=30)  # Размещение кнопки во втором окне
    msg.mainloop()

"""

def clicked(): #функция для обработки нажатия кнопки
    global t #глобальная переменная
    t=txt.get() #Считывается содержимое текстового поля
    wnd.destroy() #Закрывается окно
    
wnd=Tk() #Создание объекта окна
wnd.title("Simple Window") #Заголовок окна
wnd.geometry("500x500") #Геометрические размеры окна
wnd.resizable(False, False) #Окно постоянных размеров

fnt_1=("Arial", 13, "bold") #Шрифт 1
fnt_2=("Arial", 13, "italic") #Шрифт 2
fnt_3=("Arial", 10, "bold") #Шрифт 3

t="" #Переменная для записи текста из поля ввода

lbl = Label(master=wnd, text="Enter your name") #Создание объекта для текстовой метки
lbl.configure(font=fnt_1) #Шрифт для метки
lbl.place(x=10, y=20) #Добавление метки в окно
txt = Entry(master=wnd, width=30) #Создание объекта для поля ввода
txt.configure(font=fnt_2) #Шрифт для текста
txt.place(x=10, y=50) #Размещение текстового поля в окне
btn_1 = Button(master=wnd, text="OK") #Создание объекта первой кнопки
btn_2=Button(master=wnd, text="Cancel") #Создание объекта второй кнопки
btn_1.configure(font=fnt_3) #Шрифт для первой кнопки
btn_1.configure(command=clicked) #Команда для первой кнопки
btn_2.configure(font=fnt_3) #Шрифт для второй кнопки
btn_2.configure(command=wnd.destroy) #Команда для второй кнопки - закрытие окна
btn_1.place(x=40, y=80, width=100, height=30) #размещение первой кнопки в окне
btn_2.place(x=150, y=80, width=100, height=30) #Размещение второй кнопки в окне

wnd.mainloop() #Отображение первого окна на экране

if t!="": #Если пользователь ввел текст
    msg=Tk() #Создание объекта второго окна
    msg.title("Simple Window 2") #Заголовок окна
    msg.geometry("500x500") #Геометрические размеры окна
    msg.resizable(False, False) #Не дает изменять размеры окна
    lbl = Label(master=msg, text="Nice to meet you, "+t+"!", relief=GROOVE) #Метка с сообщением для второго окна, relief - создает рамку

    lbl.configure(font=fnt_1) #Шрифт для метки
    lbl.place(x=10, y=10, height=40, width=300) #Размещение объекта кнопки
    btn=Button(master=msg, text="OK") #Создание объекта кнопки
    btn.configure(font=fnt_3) #Шрифт для кнопки
    btn.configure(command=msg.destroy) #Метод для обработки нажатия кнопки
    btn.place(x=110, y=60, width=100, height=30) #Размещение кнопки во втором окне
    msg.mainloop() #Отображение второго окна на экране
"""