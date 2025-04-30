"""
Selectra — простое приложение для многокритериального анализа с графическим интерфейсом.
Разработано с использованием Tkinter. Поддерживает нормализацию данных, выбор приоритетов, итоговые оценки.

Авторы: ExcelPunk & Avysmorfias
Лицензия: GNU GPLv3
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def create_table():
    try:
        rows = int(entry_rows.get())
        cols = int(entry_cols.get())
        if rows <= 0 or cols <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное положительное число для строк и столбцов")
        return
    
    frame_input.pack_forget()

    global frame_table, cell_entries, column_options
    cell_entries = []
    column_options = []

    frame_table = tk.Frame(root)
    frame_table.pack(pady=10)

    # Combobox над столбцами
    for col in range(cols):
        var = tk.StringVar(value="max")
        column_options.append(var)
        label = tk.Label(frame_table, text=f"Столбец {col+1}")
        label.grid(row=0, column=col, padx=5, pady=5)
        dropdown = ttk.Combobox(frame_table, textvariable=var, values=["max", "min"], state="readonly", width=7)
        dropdown.grid(row=1, column=col, padx=5, pady=5)

    # Ячейки ввода
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            entry = tk.Entry(frame_table, width=10)
            entry.grid(row=r+2, column=c, padx=5, pady=5)

            # Навигация по ячейкам
            def move(event, row=r, col=c):
                if event.keysym == "Up" and row > 0:
                    cell_entries[row-1][col].focus_set()
                elif event.keysym == "Down" and row < rows-1:
                    cell_entries[row+1][col].focus_set()
                elif event.keysym == "Left" and col > 0:
                    cell_entries[row][col-1].focus_set()
                elif event.keysym == "Right" and col < cols-1:
                    cell_entries[row][col+1].focus_set()
                elif event.state == 4 and event.keysym == "1":  # Ctrl + 1
                    column_options[col].set("max")
                elif event.state == 4 and event.keysym == "2":  # Ctrl + 2
                    column_options[col].set("min")

            entry.bind("<KeyPress>", move)
            row_entries.append(entry)
        cell_entries.append(row_entries)

    # Кнопка Вычислить
    global btn_calc
    btn_calc = tk.Button(root, text="Вычислить", command=lambda: calculate_tables(rows, cols))
    btn_calc.pack(pady=10)
    
    # Установка фокуса на первую ячейку таблицы
    cell_entries[0][0].focus_set()

    # Enter запускает вычисления
    root.bind("<Return>", lambda e: btn_calc.invoke())

def calculate_tables(rows, cols):
    data_table = []
    try:
        for r in range(rows):
            row_data = []
            for c in range(cols):
                val = float(cell_entries[r][c].get())
                row_data.append(val)
            data_table.append(row_data)
    except ValueError:
        messagebox.showerror("Ошибка", "Убедитесь, что все ячейки заполнены числовыми значениями")
        return

    table_2 = []
    for r in range(rows):
        row2 = []
        for c in range(cols):
            col_values = [data_table[i][c] for i in range(rows)]
            if column_options[c].get() == "max":
                max_val = max(col_values)
                new_val = data_table[r][c] / max_val if max_val != 0 else 0
            elif column_options[c].get() == "min":
                min_val = min(col_values)
                new_val = min_val / data_table[r][c] if data_table[r][c] != 0 else 0
            row2.append(new_val)
        table_2.append(row2)

    column_sums = []
    for c in range(cols):
        col_sum = sum([table_2[r][c] for r in range(rows)])
        column_sums.append(col_sum)

    final_table = []
    for r in range(rows):
        row3 = []
        for c in range(cols):
            final_val = table_2[r][c] / column_sums[c] if column_sums[c] != 0 else 0
            row3.append(final_val)
        final_table.append(row3)

    modified_table = []
    for row in final_table:
        max_val = max(row)
        max_index = row.index(max_val) + 1
        new_row = []
        for c, cell_value in enumerate(row, start=0):
            if c < max_index:
                new_value = round(cell_value * (1 / max_index), 2)
            else:
                new_value = 0
            new_row.append(new_value)
        modified_table.append(new_row)

    result_window = tk.Toplevel(root)
    result_window.title("Результаты вычислений")

    tk.Label(result_window, text="Исходная таблица:").pack()
    text1 = tk.Text(result_window, height=rows+2, width=50)
    text1.pack()
    for row in data_table:
        text1.insert(tk.END, str(row) + "\n")

    tk.Label(result_window, text="Итоговая таблица:").pack()
    text4 = tk.Text(result_window, height=rows+2, width=60)
    text4.pack()
    for row in modified_table:
        row_sum = round(sum(row), 2)
        text4.insert(tk.END, f"{row} = {row_sum}\n")

# Главное окно
root = tk.Tk()
icon_path = resource_path("selectra-logo.ico")
root.iconbitmap(icon_path)

root.title("Расчёты таблицы")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Введите количество строк:").grid(row=0, column=0, padx=5, pady=5)
entry_rows = tk.Entry(frame_input, width=5)
entry_rows.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Введите количество столбцов:").grid(row=1, column=0, padx=5, pady=5)
entry_cols = tk.Entry(frame_input, width=5)
entry_cols.grid(row=1, column=1, padx=5, pady=5)

btn_create = tk.Button(frame_input, text="Создать таблицу", command=create_table)
btn_create.grid(row=2, column=0, columnspan=2, pady=10)

# Навигация стрелками между полями ввода размеров
def move_between_inputs(event):
    if event.widget == entry_rows and event.keysym == "Down":
        entry_cols.focus_set()
    elif event.widget == entry_cols and event.keysym == "Up":
        entry_rows.focus_set()

entry_rows.bind("<KeyPress>", move_between_inputs)
entry_cols.bind("<KeyPress>", move_between_inputs)


# Enter по умолчанию нажимает "Создать таблицу"
root.bind("<Return>", lambda e: btn_create.invoke())

entry_rows.focus_set()
root.mainloop()
