import time
import os
from pathlib import Path
from utils.employers import Employers
from utils.works_json import get_ids_employers
from utils.db_manager import DBManager


PATH_FILE = os.path.join(Path(__file__).parent, 'data/ids_employers.json')
PATH_DB = os.path.join(Path(__file__).parent, 'database.ini')
WORD = 'python'


def main():
    # Получить данные о работодателях и их вакансиях
    id_employers = get_ids_employers(PATH_FILE)
    employers = []
    for id_employer in id_employers:
        employers.append(Employers(id_employer))
        time.sleep(0.5)

    # код, который заполняет созданны в БД PostgreSQL
    # таблицы данными о работодателях и их вакансиях.
    db_manager = DBManager(PATH_DB)
    db_manager.create_database()
    db_manager.save_data_to_database(employers)

    # получить список всех компаний
    # и количество вакансий у каждой компании.
    result = db_manager.get_companies_and_vacancies_count()
    print(result)

    # получить список всех вакансий с указанием названия компании,
    # названия вакансии и зарплаты и ссылки на вакансию.
    result = db_manager.get_all_vacancies()
    print(result)

    # получить среднюю зарплату по вакансиям
    result = db_manager.get_avg_salary()
    print(result)

    # получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
    result = db_manager.get_vacancies_with_higher_salary()
    print(result)

    # получает список всех вакансий, в названии которых содержатся
    # переданные в метод слова, например python
    result = db_manager.get_vacancies_with_keyword(WORD)
    print(result)


if __name__ == '__main__':
    main()
