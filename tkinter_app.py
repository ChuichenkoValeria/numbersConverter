# Выполнила Чуйченко Валерия Дмитриевна. Группа . Вариант 17


import tkinter as tk
from functions import convert_numbers


def clear_entry():
    entry.delete("0", tk.END)
    result_label.config(text="")

def show_result():
    values = entry.get().split()
    result_label.config(text=convert_numbers(*values))


window = tk.Tk()

tk.Label(window, text="Введите числа через пробел").pack(padx=20, pady=(20, 0))

entry = tk.Entry(window, width=50)
entry.pack(padx=30, pady=2)

tk.Button(window, text="Очистить ввод", command=clear_entry).pack(pady=2)
tk.Button(window, text="Посчитать результат", command=show_result).pack(pady=2)

tk.Label(window, text="Результат:").pack(padx=20, pady=(2, 0))
result_label = tk.Label(window, width=50)
result_label.pack(pady=(0, 20))

window.mainloop()