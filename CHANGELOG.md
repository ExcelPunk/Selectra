# 🧭 Оглавление / Table of Contents
- [Русская версия](#русская-версия)
- [English version](#english-version)

# 📋 Changelog / История изменений

<details>
<summary>Русская версия</summary>

## [4.3] — Сборка в исполняемый файл
### Добавлено
- Программа собрана в `.exe`-файл (EXE-шник) для удобного запуска
- Добавлен логотип

---

## [4.2] — Улучшение навигации и управления
### Добавлено
- Автоматический фокус на первую ячейку при запуске программы и при переходе ко второму этапу
- Перемещение по "ячейкам" с помощью стрелок
- Горячие клавиши для выбора max/min: `CTRL + 1` и `CTRL + 2`
- Сумма значений теперь отображается в итоговой таблице

### Изменено
- Enter теперь активирует кнопку перехода к следующему этапу

---

## [4.1] — Упрощён вывод результатов
### Изменено
- Удалены таблицы 2 и 3 из окна с результатами
- Осталась только исходная таблица и таблица после последнего шага
- Добавлено округление значений до двух знаков после запятой

---

## [4.0] — Добавлена четвёртая таблица
### Добавлено
- Новый этап с четвёртой таблицей, вычисляемой по следующим правилам:
  - Если номер столбца ячейки меньше номера столбца с максимальным значением по строке:
    `1 / <номер столбца> * <значение>`
  - Иначе: `0 * <значение>`

---

## [3.0] — Минималистичный интерфейс
### Добавлено
- Графический интерфейс, в котором:
  - Пользователь вводит количество строк и столбцов
  - Выбирает значения и режим обработки (max/min)
  - Получает окно с тремя таблицами в текстовом виде

---

## [2.0] — Выбор max/min и нормализация
### Добавлено
- Возможность выбора максимального или минимального значения для каждого столбца
- Вывод трёх таблиц:
  1. Исходная таблица
  2. Таблица с нормализованными значениями:
     - При `max`: значение делится на максимум столбца
     - При `min`: минимум столбца делится на значение
  3. Итоговая таблица:
     - Ячейки из второй таблицы делятся на сумму столбца

---

## [1.0] — Первая рабочая версия
### Добавлено
- Консольное приложение
- Пользователь вводит количество строк и столбцов, затем заполняет таблицу
- Программа выводит таблицу в текстовом виде

</details>

<details>
<summary>English version</summary>

## [4.3] — Compiled executable
### Added
- Program compiled into `.exe` file for convenient launching
- Logo added

---

## [4.2] — Improved navigation and control
### Added
- Auto-focus on the first cell when the program starts and when switching to step two
- Arrow key navigation between "cells"
- Hotkeys for max/min selection: `CTRL + 1` and `CTRL + 2`
- Final table now shows the sum of values

### Changed
- Pressing Enter now triggers the button to move to the next step

---

## [4.1] — Simplified result output
### Changed
- Tables 2 and 3 removed from the results window
- Only the original and final result tables remain
- Values are now rounded to two decimal places

---

## [4.0] — Fourth table added
### Added
- New step with a fourth table, calculated as follows:
  - If the column number of a cell is less than the column number of the max value in the row:
    `1 / <column number> * <value>`
  - Otherwise: `0 * <value>`

---

## [3.0] — Minimalist interface
### Added
- Graphical interface where:
  - The user enters the number of rows and columns
  - Selects values and processing mode (max/min)
  - Gets a window with three text-based tables

---

## [2.0] — Max/min selection and normalization
### Added
- Ability to choose max or min for each column
- Three tables:
  1. Original table
  2. Normalized table:
     - If `max`: value divided by column max
     - If `min`: column min divided by value
  3. Final table:
     - Each cell from table 2 is divided by the column sum

---

## [1.0] — First working version
### Added
- Console application
- User enters number of rows and columns, then fills in the table
- Program outputs the table in text format

</details>
