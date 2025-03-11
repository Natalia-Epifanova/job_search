import logging

from src.db_manager import DBManager
from src.hh_api_request import HeadHunterAPI
from src.create_db import CreateDB
from config import config


logger = logging.getLogger("main")
file_handler = logging.FileHandler("logs/main.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

hh_api = HeadHunterAPI()
database_name = 'headhunter'
params = config()


def main():
        print('Привет! Перед вами приложение для поиска вакансий на hh.ru у интересующих вас работодателей')
        user_answer = str(input('Введите 10 или более интересующих вас вакансий через запятую: \n'))
        employers_names = user_answer.split(', ')

        vacancies_data = hh_api.fetch_vacancies_for_employers(employers_names)
        employers_data = hh_api.fetch_info_for_employers(employers_names)


        logger.info("Идет подключение к базе данных...")
        database_obj = CreateDB(database_name, params)
        database_obj.create_database()
        logger.info(f"База данных {database_name} создана успешно")
        database_obj.create_tables_in_the_database()
        logger.info("Таблицы companies и vacancies созданы успешно")
        companies_dict = database_obj.save_companies_in_tables(employers_data)
        database_obj.save_vacancies_in_tables(vacancies_data, companies_dict)
        database_obj = DBManager(database_name, params)
        while True:
                user_answer_2 = input('\nВыберите пункт меню: \n'
                                          '1. Получить список всех компаний и количество вакансий у каждой компании\n'
                                          '2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n'
                                          '3. Получить среднюю зарплату по вакансиям\n'
                                          '4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n'
                                          '5. Получить список всех вакансий, отфильтрованных по слову в названии\n'
                                          '6. Завершить программу\n')
                if not user_answer_2.isdigit() or int(user_answer_2) not in [1, 2, 3, 4, 5, 6]:
                    print('Такого пункта в меню нет. Попробуйте снова')
                elif int(user_answer_2) == 1:
                    database_obj.get_companies_and_vacancies_count()
                elif int(user_answer_2) == 2:
                    database_obj.get_all_vacancies()
                elif int(user_answer_2) == 3:
                    database_obj.get_avg_salary()
                elif int(user_answer_2) == 4:
                    database_obj.get_vacancies_with_higher_salary()
                elif int(user_answer_2) == 5:
                    user_answer_3 = str(input('Введите слово для фильтрации: \n'))
                    database_obj.get_vacancies_with_keyword(user_answer_3)
                elif int(user_answer_2) == 6:
                    break


if __name__ == "__main__":
    main()

    #Яндекс, Ростелеком, Т-Банк, Альфа-Банк, МТС, VK, Ozon, WILDBERRIES, Газпром нефть, Лукойл