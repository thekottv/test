from tkinter import *
from tkinter import messagebox

window = Tk()  # Создаем экземпляр tkinter

"""Конструктор окна"""
window.iconbitmap(r"images/image.ico")  # Иконка окна
window.title("Авторизация")  # Заголовок окна
window.geometry("450x230")  # Длина и ширина окна
window.resizable(False, False)  # Явный запрет изменять размеры окна
window.configure(bg='#FFFFFF')
font_header = ("Arial", 20)  # Шрифт "Times New Roman" с размером 15 для заголовка
font_entry = ("Arial", 14)  # Шрифт "Times New Roman" с размером 12 для заголовка
label_font = ("Arial", 14)  # Шрифт "Times New Roman" с размером 11 для заголовка
base_padding = {"padx": 10, "pady": 8}  # Отступы: по горизонтали:10, по вертикали: 8
header_padding = {"padx": 10, "pady": 12}  # Отступы заголовка: по горизонтали: 10, по вертикали: 12

"""Элементы окна"""
main_label = Label(window, text="Авторизация", font=font_header, justify=CENTER, **header_padding)  # "Авторизация"
username_entry = Entry(window, bg="#fff", fg="#444", font=font_entry)  # Поле ввода имени пользователя
username_label = Label(window, text="Имя пользователя", font=label_font, **base_padding)  # Заголовок "Имя пользователя"
password_entry = Entry(window, bg="#fff", fg="#444", font=font_entry)  # Поле ввода пароля
password_label = Label(window, text="Пароль", font=label_font, **base_padding)  # Заголовок "Пароль"


def clicked():
    """Обработчик нажатия кнопки 'Войти'"""
    username = username_entry.get()  # Получаем имя пользователя
    password = password_entry.get()  # Получаем пароль

    # Показываем месседжбокс с веденными именем пользователя и паролем
    messagebox.showinfo("Заголовок", "{username}, {password}".format(username=username, password=password))


send_btn = Button(window, text="Войти", command=clicked)  # Кнопка авторизации

"""Отрисовываем элементы"""
main_label.pack()  # Рисуем заголовок "Авторизация"
username_label.pack()  # Рисуем заголовок "Имя пользователя"
username_entry.pack()  # Рисуем поле ввода имени пользователя
password_label.pack()  # Рисуем заголовок "Пароль"
password_entry.pack()  # Рисуем поле ввода пароля
send_btn.pack(**base_padding)  # Рисуем кнопку авторизации

window.mainloop()  # Запускаем окно
