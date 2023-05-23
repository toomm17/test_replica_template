import psycopg2




def have_table_in_db(table_name: str):
    conn = psycopg2.connect(dbname='postgres',
                            user='psiko',
                            password='psikod',
                            host='10.55.71.18',
                            port='5432')

    cursor = conn.cursor()

    cursor.execute("SELECT table_name FROM information_schema.tables"
                   "WHERE table_schema NOT IN ('information_schema', 'pg_catalog')"
                   "AND table_schema IN('public', 'myschema')")
    for res in cursor.fetchall():
        if table_name in res:
            return True
        else:
            return False

    cursor.close()
    conn.close()
    print('Подключение закрыто')

def insert_into_table(values: tuple):
    conn = psycopg2.connect(dbname='postgres',
                            user='psiko',
                            password='psikod',
                            host='10.55.71.18',
                            port='5432')
    print('Подключение установлено')
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO public.test_19896463 (id, name) VALUES {values}")
    conn.commit()
    print('Данные добавлены')
    """
        Селект просто для проверки пока что
    """
    cursor.execute("SELECT * FROM public.test_19896463")
    print(cursor.fetchall())

    cursor.close()
    conn.close()
    print('Подключение закрыто')