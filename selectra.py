# Шаг 1: Ввод исходных данных
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

data_table = []
for i in range(rows):
    row_data = []
    for j in range(cols):
        value = float(input(f"Введите число для ячейки ({i+1}, {j+1}): "))
        row_data.append(value)
    data_table.append(row_data)

# Шаг 2: Запрос направления (max/min) для каждого столбца и расчёт таблицы 2
column_preferences = []
for j in range(cols):
    while True:
        pref = input(f"Столбец {j+1}: хотите ли вычислять по max или min? Введите 'max' или 'min': ").strip().lower()
        if pref in ['max', 'min']:
            column_preferences.append(pref)
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")

table_2 = []
for i in range(rows):
    row_2 = []
    for j in range(cols):
        col_values = [data_table[k][j] for k in range(rows)]
        if column_preferences[j] == 'max':
            max_val = max(col_values)
            if max_val != 0:
                new_val = data_table[i][j] / max_val
            else:
                new_val = 0
        elif column_preferences[j] == 'min':
            min_val = min(col_values)
            if data_table[i][j] != 0:
                new_val = min_val / data_table[i][j]
            else:
                new_val = 0
        row_2.append(new_val)
    table_2.append(row_2)

# Шаг 3: Расчёт итоговой таблицы (деление на сумму по столбцу таблицы 2)
column_sums = []
for j in range(cols):
    col_sum = sum([table_2[i][j] for i in range(rows)])
    column_sums.append(col_sum)

final_table = []
for i in range(rows):
    final_row = []
    for j in range(cols):
        if column_sums[j] != 0:
            final_val = table_2[i][j] / column_sums[j]
        else:
            final_val = 0
        final_row.append(final_val)
    final_table.append(final_row)

# Вывод результатов
print("\nИсходная таблица:")
for row in data_table:
    print(row)

print("\nТаблица после расчётов шага 2:")
for row in table_2:
    print(row)

print("\nИтоговая таблица после шага 3:")
for row in final_table:
    print(row)
