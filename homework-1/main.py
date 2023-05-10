"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

from settings import EMPLOYEES, CUSTOMERS, ORDERS

conn = psycopg2.connect(host='localhost', database='north', user='cheatbarspin', password='1053')
try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany('insert into employees values (%s, %s, %s, %s, %s, %s)',
                            [('1', 'Alexander', 'Bogdad', 'Resaler', '1970-02-12', 'text_1'),
                             ('2', 'Peter', 'Parker', 'Owner', '1982-11-12', 'text_2'),
                             ('3', 'Alehandro', 'Ankara', 'Coworker', '1999-03-12', 'text_3')]
                            )
            cur.executemany('insert into customers values (%s, %s, %s)',
                            [('ALFKI', 'Alfreds Futterkiste', 'Maria Anders'),
                             ('ANATR', 'Ana Trujillo Emparedados y helados', 'Ana Trujillo'),
                             ('ANTON', 'Antonio Moreno Taquería', 'Antonio Moreno')]
                            )
            cur.executemany('insert into orders values (%s, %s, %s, %s, %s)',
                            [('10001', 'ALFKI', '2', '2023-03-22', 'Riga'),
                             ('10002', 'ALFKI', '2', '2023-03-23', 'Riga'),
                             ('10003', 'ANTON', '1', '2023-04-01', 'London')]
                            )


finally:
    conn.close()

# Методы вывода для проверки
# cur.execute('SELECT * FROM employees')
# cur.execute('SELECT * FROM customers')
# cur.execute('SELECT * FROM orders')
