

def test_postgres_connection(postgres, test_for_igor):
    print('Стартуем тест функцию')
    print(test_for_igor, 'TEST FOR IGOR VALUE IN TEST')
    with postgres.cursor() as cursor:
        cursor.execute('SELECT * FROM Shemet')
        print(cursor.fetchall())

        postgres.commit()

    print('Тест функция закрывается ....')



