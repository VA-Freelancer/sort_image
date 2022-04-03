from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import datetime


def choose_dir():  # создаем функцию  для выбора папки
    pass


def f_start():  # создаем функцию для начала обработки
    pass


root = Tk()
root.title("Image Sort")  # задаем заголовок
root.iconbitmap("image.ico")  # задаем иконку
root.geometry("500x500")  # задаем размер

s = ttk.Style()
s.configure('vp.TButton', font=("Helvetica", 15))

frame = Frame(root, bg="#56ADFF", bd=5)  # создаем фрейм, добавляем цвет и 
frame.pack(padx=10, pady=10, fill=X)  # упаковываем, указываем сторону, растягиваем по x

e_path = ttk.Entry(frame)  # создаем поле ввода и размещаем во фрейме
e_path.pack(side=LEFT, ipady=2, expand=True, fill=X)  # упаковываем, добавляем растягтвание по X

# создаем кнопку и размещаю её во фрейме, добавляю название и привязываю функцию
btn_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_dir)

btn_dialog.pack(side=LEFT, padx=5)  # упаковываем кнопку и центруем по левой стороне

# создаем кнопку и размещаем её в окне, добавляю название и привязываю функцию
btn_start = ttk.Button(root, text="Старт", style="vp.TButton", command=f_start)

btn_start.pack(fill=X, padx=10)  # упаковываем кнопку и центруем по левой стороне

root.mainloop()  # запускаем цикл
