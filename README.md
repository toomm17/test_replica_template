В этом проекте реализованы автотесты для ETL4HADOOP.

ETL4Hadoop - это проект по репликации данных.

Основные сущности в проекте на данный момент (5/20/2023):
    1) Поток - полностью готовая к запуску репликация данных. Запускается в отдельном потоке.
    2) Источник - 


Задачи, которые необходимо реализовать (до 5/28/2023):
    1) Возможность формирования списка потоков
    2) Возможность указания сколько потоков могут работать одновременно
    3) Разработать функционал добавления записей в таблицу источника

Условные обозначения:
    1) REPL_THR (repl_thr) или THR (в зависимости от контекста) - репликационный поток, одна из основых сущностей ETL4Hadoop
    2) 


Реализация задачи по формированию списка потоков:
    1) Создать конфигурационный файл - config.json в корне проекта, внутри которого будем указывать список с именами потоков и прочие настройки.

    Арихитектура config.json (будет обновляться):
    {
        'threads': {
            'list': [
                {
                    "name": "first_name",
                    "insert_row_in_table": true,
                    "is_single_run": true
                },
                {
                    "name": "second_name",
                    "insert_row_in_table": false,
                    "is_single_run": true
                },
                {
                    "name": "third_name",
                    "insert_row_in_table": false,
                    "is_single_run": false
                }
            ],
        }
    }

    name - Имя потока
    insert_row_in_table - Нужно ли перед стартом потока, добавить запись в таблицу (скорее всего изменится)
    is_single_run - Запуск потока будет однопоточно/паралелльно
    
    Ограничения:
        list - список не может быть пустым

    2) Реализация получения данных из config.json средствами python - модуль json.


Реализация задачи по указанию количества потоков, которые могут работать одновременно:
    1) В config.json указываем максимально число запущенных потоков.
    2) Реализовать одновременный запуск потоков на python - модуль threading.
