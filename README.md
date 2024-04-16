# Парсер PEP by Scrapy
### Описание
Благодаря этому проекту можно будет развить знание языка Python сопровождается документами PEP — Python Enhancement Proposal. С одним из этих документов многие знакомы — это PEP 8, рекомендации по оформлению кода. Парсер документов PEP на базе фреймворка Scrapy. Парсер собирает информацию о статусах PEP и сохраняет результаты в csv-файл.
- Парсер документации PEP на базе фреймворка Scrapy.
- Парсер собирает информацию со страницы https://peps.python.org/
- Парсер выводит собранную информацию в два файла .csv
### Технологии
- Python 3.9
- SQLAlchemy 2.0.29
- Scrapy 2.5.1
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Выполните команду:
```
scrapy crawl pep
```
### Создание описания
```
Описание проекта было создано при помощи сайта readme.so/editor
```
### Автор
Артём Карташян
#### (https://github.com/yhtrg)