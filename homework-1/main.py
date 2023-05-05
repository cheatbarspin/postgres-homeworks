"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

from settings import EMPLOYEES, CUSTOMERS, ORDERS

conn = psycopg2.connect(host='localhost', database='north', user='cheatbarspin', password='1053')
# try:
#     with conn:
#         with conn.cursor() as cur:
#             with open(EMPLOYEES, 'r') as f:
#                 next(f)
#                 cur.copy_from(f, 'employees', sep=",")
# finally:
#     conn.close()

try:
    with conn:
        with conn.cursor() as cur:
            with open(CUSTOMERS, 'r') as f:
                next(f)
                cur.copy_from(f, 'customers', sep=",")
finally:
    conn.close()

# try:
#     with conn:
#         with conn.cursor() as cur:
#             with open(ORDERS, 'r') as f:
#                 next(f)
#                 cur.copy_from(f, 'orders', sep=",")
# finally:
#     conn.close()

# Методы вывода для проверки
# cur.execute('SELECT * FROM employees')
# cur.execute('SELECT * FROM customers')
# cur.execute('SELECT * FROM orders')
