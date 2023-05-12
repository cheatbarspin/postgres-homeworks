"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2, csv

from settings import EMPLOYEES, CUSTOMERS, ORDERS

conn = psycopg2.connect(host='localhost', database='north', user='cheatbarspin', password='1053')
try:
    with conn:
        with conn.cursor() as cur:
            with open(CUSTOMERS) as file:  # Открыть customers_data
                file_reader = csv.DictReader(file, delimiter=',')

                for row in file_reader:
                    customer_id = row.get('customer_id')
                    company_name = row.get('company_name')
                    contact_name = row.get('contact_name')

                    cur.executemany(
                        'INSERT INTO customers VALUES (%s, %s, %s)',
                        [(customer_id, company_name, contact_name)])

            with open(EMPLOYEES) as file:  # Открыть employees_data
                file_reader = csv.DictReader(file, delimiter=',')

                for row in file_reader:
                    first_name = row.get('first_name')
                    last_name = row.get('last_name')
                    title = row.get('title')
                    birth_date = row.get('birth_date')
                    notes = row.get('notes')

                    cur.executemany(
                        'INSERT INTO employees VALUES (default, %s, %s, %s, %s, %s)',
                        [(first_name, last_name, title, birth_date, notes)])

            with open(ORDERS) as file:  # Открыть orders_data
                file_reader = csv.DictReader(file, delimiter=',')

                for row in file_reader:
                    order_id = row.get('order_id')
                    customer_id = row.get('customer_id')
                    employee_id = row.get('employee_id')
                    order_date = row.get('order_date')
                    ship_city = row.get('ship_city')

                    cur.executemany(
                        'INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                        [(order_id, customer_id, employee_id, order_date, ship_city)])

finally:
    conn.close()

# Методы вывода для проверки
# cur.execute('SELECT * FROM employees')
# cur.execute('SELECT * FROM customers')
# cur.execute('SELECT * FROM orders')
