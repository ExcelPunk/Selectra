import tkinter as tk
from tkinter import ttk, messagebox

def create_table():
    """
    Функция считывает введённые пользователем значения для количества строк
    и столбцов, затем создаёт динамически окно с таблицей ввода.
    В заголовке для каждого столбца появляется выпадающий список (Combobox)
    для выбора режима расчёта: «max» или «min».
    """
    try:
        rows = int(entry_rows.get())
        cols = int(entry_cols.get())
        if rows <= 0 or cols <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное положительное число для строк и столбцов")
        return

    # Скрываем фрейм ввода исходных размеров
    frame_input.pack_forget()

    # Создаем новый фрейм для ввода таблицы
    global frame_table, cell_entries, column_options
    cell_entries = []      # двумерный список для полей ввода значений таблицы
    column_options = []    # список переменных, связанных с выпадающими списками для столбцов

    frame_table = tk.Frame(root)
    frame_table.pack(pady=10)

    # Создаем "заголовок" таблицы: для каждого столбца располагаем ярлык и выпадающий список
    for col in range(cols):
        var = tk.StringVar(value="max")  # по умолчанию значение "max"
        column_options.append(var)        # сохраняем переменную для последующего доступа
        label = tk.Label(frame_table, text=f"Столбец {col+1}")
        label.grid(row=0, column=col, padx=5, pady=5)
        # Выпадающий список с вариантами «max» и «min»
        dropdown = ttk.Combobox(frame_table, textvariable=var, values=["max", "min"], state="readonly", width=7)
        dropdown.grid(row=1, column=col, padx=5, pady=5)

    # Создаем поля ввода для каждой ячейки (расположены ниже заголовка)
    for r in range(rows):
        row_entries = []
        for c in range(cols):
            entry = tk.Entry(frame_table, width=10)
            entry.grid(row=r+2, column=c, padx=5, pady=5)
            row_entries.append(entry)
        cell_entries.append(row_entries)

    # Кнопка для запуска расчётов, которая расположена ниже таблицы ввода
    btn_calc = tk.Button(root, text="Вычислить", command=lambda: calculate_tables(rows, cols))
    btn_calc.pack(pady=10)

def calculate_tables(rows, cols):
    """
    Функция собирает введённые значения из полей ввода и выполняет расчёты:
    1. Для каждого столбца в зависимости от выбранного значения (max/min)
       высчитывается новая таблица (таблица 2).
    2. Затем каждая ячейка таблицы 2 делится на сумму значений своего столбца (итоговая таблица).
    После расчетов результаты отображаются в новом окне.
    """
    # Сбор данных из таблицы ввода
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

    # Шаг 2: Расчет таблицы 2 по выбранным условиям для каждого столбца
    table_2 = []
    for r in range(rows):
        row2 = []
        for c in range(cols):
            # Собираем данные для столбца c
            col_values = [data_table[i][c] for i in range(rows)]
            if column_options[c].get() == "max":
                max_val = max(col_values)
                # Делим значение на максимум (с проверкой на деление на ноль)
                new_val = data_table[r][c] / max_val if max_val != 0 else 0
            elif column_options[c].get() == "min":
                min_val = min(col_values)
                # Делим минимум на значение ячейки (с проверкой на деление на ноль)
                new_val = min_val / data_table[r][c] if data_table[r][c] != 0 else 0
            row2.append(new_val)
        table_2.append(row2)

    # Шаг 3: Итоговая таблица – делим каждую ячейку таблицы 2 на сумму значений в столбце
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

    # Шаг 4: Применяем новую операцию по строкам
    # Для каждой строки найдём номер столбца с максимальным значением.
    # Будем считать, что нумерация столбцов начинается с 1.
    modified_table = []  # новая таблица с результатом операции

    for row in final_table:
        # Находим максимальное значение и его индекс (если максимум встречается несколько раз, берём первый)
        max_val = max(row)
        max_index = row.index(max_val) + 1  # +1 чтобы получить номер столбца (не индекс)
        
        new_row = []
        # Для каждого элемента в строке:
        for c, cell_value in enumerate(row, start=0):  # начинаем нумерацию с 1
            if c < max_index:
                new_value = cell_value * (1 / max_index)
            else:
                new_value = cell_value * 0
            new_row.append(new_value)
        modified_table.append(new_row)

    # Отображение результатов в новом окне
    result_window = tk.Toplevel(root)
    result_window.title("Результаты вычислений")

    # Вывод исходной таблицы
    tk.Label(result_window, text="Исходная таблица:").pack()
    text1 = tk.Text(result_window, height=rows+2, width=50)
    text1.pack()
    for row in data_table:
        text1.insert(tk.END, str(row) + "\n")

    # Вывод таблицы после шага 2
    tk.Label(result_window, text="Таблица после шага 2:").pack()
    text2 = tk.Text(result_window, height=rows+2, width=50)
    text2.pack()
    for row in table_2:
        text2.insert(tk.END, str(row) + "\n")

    # Вывод итоговой таблицы после шага 3
    tk.Label(result_window, text="Итоговая таблица после шага 3:").pack()
    text3 = tk.Text(result_window, height=rows+2, width=50)
    text3.pack()
    for row in final_table:
        text3.insert(tk.END, str(row) + "\n")
        
    # Вывод новой таблицы после дополнительной операции
    tk.Label(result_window, text="Итоговая таблица после дополнительной операции:").pack()
    text4 = tk.Text(result_window, height=rows+2, width=50)
    text4.pack()
    for row in modified_table:
        text4.insert(tk.END, str(row) + "\n")


# Основное окно приложения
root = tk.Tk()
root.title("Расчёты таблицы")

# Фрейм для первоначального ввода количества строк и столбцов
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

root.mainloop()
