import sqlite3


with sqlite3.connect('db_test.sqlite') as conn:
    cur = conn.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS directors(
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            birth_day INTEGER
        );

        CREATE TABLE IF NOT EXISTS video_products(
            id INTEGER PRIMARY KEY,
            title TEXT,
            product_type TEXT,
            release_year INTEGER
        );

    '''
    cur.executescript(query)
    conn.commit()

    directors = [
        (1, 'Текс Эйвери', 1908),
        (2, 'Роберт Земекис', 1952),
        (3, 'Джерри Чиникей', 1912),
    ]
    video_products = [
        (1, 'Весёлые мелодии', 'Мультсериал', 1930),
        (2, 'Кто подставил кролика Роджера', 'Фильм', 1988),
        (3, 'Безумные мелодии Луни Тюнз', 'Мультсериал', 1931),
        (4, 'Розовая пантера: Контроль за вредителями', 'Мультфильм', 1969)
    ]

    cur.executemany('INSERT INTO directors VALUES(?, ?, ?);', directors)
    cur.executemany('INSERT INTO video_products VALUES(?, ?, ?, ?);',
                    video_products
                    )
    conn.commit()
