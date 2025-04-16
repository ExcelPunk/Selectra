# Запрашиваем у пользователя размеры таблицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создаем пустую таблицу
table = []

# Заполняем таблицу данными от пользователя
for i in range(rows):
    row = []
    for j in range(cols):
        value = float(input(f"Введите число для ячейки ({i+1}, {j+1}): "))
        row.append(value)
    table.append(row)

# Выводим таблицу
print("\nПолученная таблица:")
for row in table:
    print(row)
