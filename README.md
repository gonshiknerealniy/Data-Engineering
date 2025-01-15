# База данных по синтезу фармацевтических сокристаллов методом измельчения с растворителем

## О  проекте

Сокристаллы — это кристаллические материалы, состоящие из двух или более разных молекул, обычно активного фармацевтического ингредиента (АФИ) и сокристаллических формеров («коформеров»), в одной и той же кристаллической решетке. Фармацевтические сокристаллы предоставили возможность для создания твердофазных форм в дополнение к стандартным твердофазным формам АФИ, таким как соли и полиморфы. Сокристаллы можно создавать для повышения биодоступности и стабильности лекарственного препарата, а также для повышения обрабатываемости АФИ во время производства лекарственного препарата.

 На сегодняшний день данные о синтезе сокристаллов часто разбросаны по научным статьям, что затрудняет их анализ и использование. База данных позволит централизовать информацию об условиях проведения синтеза.

 Домен: химия, фармацевтическая технология

## Содержание

### Сбор данных

Информация собрана мною вручную из публикаций научных журналов Q1 и находится в файле lag_data.csv.

### Проверка и очистка данных

В процессе создания базы данных вносилось много корректировок относительно экстрагируемых параметров, поскольку в разных статьях имеется довольно большой разрыв предоставляемой информации по синтезу.

В итоге, из параметров решила оставить:

1. doi статьи
2. API - активный фармацевтический компонент
3. cof1 - коформер (в процессе сбора информации приняла решение использовать  только двоичные системы)
4. ratio, mol - молярное соотношение API к cof1
5. liquid - растворитель
6. liq/coc ratio - соотношение растворителя к смеси реагентов
7. mixing apparatus - смешивающий аппарат
8. mixing frequency, Hz - частота перемешивания, герц
9. mixing temp, C - температура перемешивания, градусы Цельсия
10. mixing time, min - время перемешивания, минуты
11. drying time, h - время сушки, часы
12. drying temp, C - температура сушки, градусы Цельсия
13. text - текст методики синтеза
    
### EDA

Исследовательский анализ проведен в файле eda.ipynb

Также, в этом файле находится предобработка данных - заполнение пропусков, нормализация и небольшая статистика по базе.


### Метрики качества данных

#### Содержание данных

Валидность - соответствие многочисленным атрибутам, связанных с элементом данных: тип, точность, формат, диапазоны допустимых значений и так далее.

1. doi - текст
2. API - текст
3. cof1 - текст
4. ratio, mol - число с плавающей точкой
5. liquid - текст
6. liq/coc ratio - число с плавающей точкой
7. mixing apparatus - смешивающий аппарат
8. mixing frequency, Hz - число с плавающей точкой
9. mixing temp, C - число с плавающей точкой
10. mixing time, min - число с плавающей точкой
11. drying time, h - число с плавающей точкой
12. drying temp, C - число с плавающей точкой

#### Согласованность

Уникальность - ни один объект не существует в наборе данных более одного раза. Наличие дублей может приводить к несогласованности и противоречиям вследствие отсутствия единой версии правды.

Согласованность - соответствие данных друг другу и их логическая непротиворечивость.

Значения API, cof1 и liquid должны соответствовать реальным молекулам и создавать уникальные комбинации.

### Разработка БД

Для хранения данных была выбрана СУБД SQLite. Данные из csv-файла и из датафрейма переносятся в базу посредством скрипта, использующего встроенный модуль sqlite3.

### Дашборд

Интерактивный дашборд формируется с помощью билиотеки Dash.

### Автоматизировнный пайплайн

Находится в файле pipeline.py. Требования в requirements.txt 

Как работает пайплайн:

1. Проверяет наличие исходного файла lag_data.csv.
2. Запускает Jupyter Notebook для обработки данных.
3. Проверяет, что файл lag_data_new.csv был создан.
4. Загружает данные из lag_data_new.csv в базу данных synthesis.db.
5. Логирует завершение работы.

# Цели

Актуальной задачей моего проекта является увеличение базы данных с помощью автопарсинга научных статей (с помощью модели openai/gpt-3.5-turbo). В дальнейшем, планируется включить и другие методики синтеза сокристаллов, а также включить в нее данные по кристаллическим структурам полученных веществ, что станет крайне полезным продуктом для многих ученых, работающих с сокристаллами.

# Выводы

За время работы над проектом, хотя результат и не достиг ожидаемого уровня, я приобрела много ценных навыков и значительный опыт, который поможет мне в дальнейших задачах. Я особенно благодарна преподавателям за поддержку, знания и возможность попробовать себя в новом направлении. Этот проект стал для меня важным шагом в развитии моих профессиональных компетенций.
