# Файл для создания переменных путей
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
EMPLOYEES = Path.joinpath(CURRENT_DIR, 'homework-1', 'north_data', 'employees_data.csv')
CUSTOMERS = Path.joinpath(CURRENT_DIR, 'homework-1', 'north_data', 'customers_data.csv')
ORDERS = Path.joinpath(CURRENT_DIR, 'homework-1', 'north_data', 'orders_data.csv')
