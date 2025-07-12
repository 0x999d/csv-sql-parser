# CSV SQL Parser

![Тесты](https://img.shields.io/badge/tests-passing-brightgreen)

CSV SQL Parser — это инструмент для анализа и обработки файлов .csv с поддержкой условий `WHERE`, агрегатных функций (`MIN`, `MAX`, `AVG`) и сортировки (`ORDER BY`). Позволяет легко извлекать и обрабатывать данные из .csv файлов с помощью простого синтаксиса похожим на SQL.

## Установка

Для установки необходимо клонировать репозиторий и установить зависимости

   ```bash
   git clone https://github.com/0x999d/csv-sql-parser.git
   cd csv-sql-parser
   pip install -r requirements.txt
```
## Зависимости
Из зависимостей, которые необходимо установить используется только `prettytable` для красивого вывода текста. 

Также необходим Python версии позднее `3.10`

### Параметры запуска & возможности
* --where Column>5, например `Age>25`. Принимает `>`, `<`, `=`, `<=`, `>=`. 
* --aggregate Column=avg, например `Age=avg`. Принимает `avg`, `min`, `max`
* --order-by Column=asc, например `Age=asc`. Принимает `asc`, `desc`

Можно групировать флаги, например `--where Age>20 --order-by Age=asc`

### Тесты
Запустить тесты можно при помощи `pytest`, командой 
```bash
pytest tests
```

#### Скриншоты
* Обычное использование
  
  ![Default usage](https://github.com/0x999d/csv-sql-parser/blob/master/files/default.png)

* Оператор where

  ![where usage](https://github.com/0x999d/csv-sql-parser/blob/master/files/where.png)

* Оператор aggregate

  ![aggregate usage](https://github.com/0x999d/csv-sql-parser/blob/master/files/aggregate.png)

* Сортировка order by

  ![aggregate usage](https://github.com/0x999d/csv-sql-parser/blob/master/files/orderby.png)
