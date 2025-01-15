import os
import subprocess
import sqlite3
import pandas as pd

# Путь к файлам
DATA_FILE = "lag_data.csv"
NEW_DATA_FILE = "lag_data_new.csv"
DB_FILE = "synthesis.db"
NOTEBOOK_FILE = "eda.ipynb"


def run_notebook(notebook_path):
    """
    Запускаем Jupyter Notebook с использованием nbconvert.
    """
    print("Запуск обработки данных в Jupyter Notebook...")
    subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            notebook_path,
            "--output",
            notebook_path,
        ]
    )


def load_data_to_db(lag_data_new_path, db_path):
    """
    Загружаем данные из new_data.csv в SQLite базу данных.
    """
    print("Загрузка обработанных данных в базу данных...")
    # Читаем обработанные данные
    df = pd.read_csv(lag_data_new_path)

    # Подключаемся к базе данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создаем таблицу (если еще не создана)
    table_name = "processed_data"
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    print(f"Данные успешно загружены в таблицу '{table_name}'")
    conn.close()


def main():
    """
    Основной пайплайн обработки данных.
    """
    print("Запуск пайплайна...")

    # 1. Проверяем наличие исходных данных
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Исходный файл данных {DATA_FILE} не найден.")

    # 2. Запуск обработки данных в Jupyter Notebook
    run_notebook(NOTEBOOK_FILE)

    # 3. Проверяем, что обработанный файл создан
    if not os.path.exists(NEW_DATA_FILE):
        raise FileNotFoundError(f"Обработанный файл {NEW_DATA_FILE} не создан.")

    # 4. Загружаем обработанные данные в базу
    load_data_to_db(NEW_DATA_FILE, DB_FILE)

    print("Пайплайн выполнен успешно.")


if __name__ == "__main__":
    main()
