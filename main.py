
from tkinter import *
from test_class_1 import Gemogramm

def clicked():
    global sex
    global hemoglobin
    global erythrocytes
    global reticulocytes
    global thrombocytes
    global leukocyte
    sex=txt_1.get()
    hemoglobin=txt_2.get()
    erythrocytes=txt_3.get()
    reticulocytes=txt_4.get()
    thrombocytes=txt_5.get()
    leukocyte=txt_6.get()
    wnd.destroy()

wnd = Tk()
wnd.title("Gemoramm")
wnd.geometry("500x500")
wnd.resizable(False, False)
fnt_1 = ("Arial", 13, "bold")  # Шрифт 1
fnt_2 = ("Arial", 13, "italic")  # Шрифт 2
fnt_3 = ("Arial", 10, "bold")  # Шрифт 3

sex = ''
hemoglobin = ''
erythrocytes = ''
reticulocytes = ''
thrombocytes = ''
leukocyte = ''

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

lbl_6 = Label(master=wnd, text="Введите показатель лейкоцитов: ")
lbl_6.configure(font=fnt_1)
lbl_6.place(x=10, y=310)
txt_6 = Entry(master=wnd, width=30)
txt_6.configure(font=fnt_2)
txt_6.place(x=10, y=340)

btn_1 = Button(master=wnd, text="OK")  # Создание объекта первой кнопки
btn_2 = Button(master=wnd, text="Cancel")  # Создание объекта второй кнопки
btn_1.configure(font=fnt_3)  # Шрифт для первой кнопки
btn_1.configure(command=clicked)  # Команда для первой кнопки
btn_2.configure(font=fnt_3)  # Шрифт для второй кнопки
btn_2.configure(command=wnd.destroy)  # Команда для второй кнопки - закрытие окна
btn_1.place(x=40, y=370, width=100, height=30)  # размещение первой кнопки в окне
btn_2.place(x=150, y=370, width=100, height=30)

wnd.mainloop()

if sex!="" and hemoglobin!="" and erythrocytes!="" and reticulocytes!="" and thrombocytes!="" and leukocyte!="":
    msg = Tk()  # Создание объекта второго окна
    msg.title("Gemogramm")  # Заголовок окна
    msg.geometry("500x500")  # Геометрические размеры окна
    msg.resizable(False, False)

    result = Gemogramm(sex, hemoglobin, erythrocytes, reticulocytes, thrombocytes, leukocyte)
    diagnose_text = result.get_diagnosis_string()

    lbl = Label(master=msg, text=diagnose_text,relief=GROOVE)  # Метка с сообщением для второго окна, relief - создает рамку

    lbl.configure(font=fnt_1)  # Шрифт для метки
    lbl.place(x=10, y=10, height=100, width=480)  # Размещение объекта кнопки
    btn = Button(master=msg, text="OK")  # Создание объекта кнопки
    btn.configure(font=fnt_3)  # Шрифт для кнопки
    btn.configure(command=msg.destroy)  # Метод для обработки нажатия кнопки
    btn.place(x=200, y=120, width=100, height=30)  # Размещение кнопки во втором окне
    msg.mainloop()


