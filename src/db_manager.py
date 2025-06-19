from contextlib import closing
from typing import Any

import psycopg2


class DBManager:
    """Класс для запросов к базе данных"""

    database_name: str
    params: dict

    def __init__(self, database_name: str, params: dict) -> None:
        """Инициализация класса"""
        self.database_name = database_name
        self.params = params

    def __connect_to_db(self) -> Any:
        """Создает соединение с базой данных. Возвращает объект соединения."""
        return psycopg2.connect(dbname=self.database_name, **self.params)

    def __execute_query(self, query: str, params=None) -> Any:
        """Общий метод для выполнения SQL-запроса"""
        with closing(self.__connect_to_db()) as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchall()

    def get_companies_and_vacancies_count(self) -> None:
        """Метод для получения списка всех компаний и количества вакансий у каждой компании"""
        query = """
            SELECT companies.company_name, COUNT(vacancies.vacancy_id)
            FROM companies
            LEFT JOIN vacancies USING(company_id)
            GROUP BY companies.company_name;
        """
        rows = self.__execute_query(query)
        for row in rows:
            print(row)

    def get_all_vacancies(self) -> None:
        """Метод для получения списка всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию"""
        query = """
            SELECT companies.company_name, vacancies.vacancy_name,
               CASE
                   WHEN vacancies.salary_from = 0 THEN 'Не указано'
                   ELSE CAST(vacancies.salary_from AS TEXT)
               END AS salary_from,
               CASE
                   WHEN vacancies.salary_to = 0 THEN 'Не указано'
                   ELSE CAST(vacancies.salary_to AS TEXT)
               END AS salary_to,
               vacancies.description_url_hh
            FROM vacancies
            INNER JOIN companies USING(company_id);
            """
        rows = self.__execute_query(query)
        for row in rows:
            print(row)

    def get_avg_salary(self) -> None:
        """Метод для получения средней зарплаты по вакансиям"""
        query = """
            SELECT AVG(salary_from)
            FROM vacancies
            WHERE salary_from > 0;
        """
        rows = self.__execute_query(query)
        for row in rows:
            print(row)

    def get_vacancies_with_higher_salary(self) -> None:
        """Метод для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        query = """
            SELECT companies.company_name, vacancies.vacancy_name,
                CASE
                   WHEN vacancies.salary_from = 0 THEN 'Не указано'
                   ELSE CAST(vacancies.salary_from AS TEXT)
                END AS salary_from,
                CASE
                   WHEN vacancies.salary_to = 0 THEN 'Не указано'
                   ELSE CAST(vacancies.salary_to AS TEXT)
                END AS salary_to,
                vacancies.description_url_hh
            FROM vacancies
            INNER JOIN companies USING(company_id)
            WHERE (vacancies.salary_from > (SELECT AVG(salary_from) FROM vacancies WHERE salary_from > 0)
            OR vacancies.salary_to > (SELECT AVG(salary_from) FROM vacancies WHERE salary_from > 0));
        """
        rows = self.__execute_query(query)
        for row in rows:
            print(row)

    def get_vacancies_with_keyword(self, keywords: str) -> None:
        """Метод для получения списка всех вакансий, в названии которых содержатся переданные в метод слова"""
        keywords_list = keywords.split()
        like_conditions = " OR ".join([f"vacancies.vacancy_name ILIKE %s" for _ in keywords_list])

        query = f"""
            SELECT companies.company_name, vacancies.vacancy_name,
                CASE
                   WHEN vacancies.salary_from = 0 THEN 'Не указано'
                   ELSE CAST(vacancies.salary_from AS TEXT)
                END AS salary_from,
                CASE
                   WHEN vacancies.salary_to = 0 THEN 'Не указано'
                   ELSE CAST(vacancies.salary_to AS TEXT)
                END AS salary_to,
                vacancies.description_url_hh
            FROM vacancies
            INNER JOIN companies USING(company_id)
            WHERE {like_conditions};
        """
        params = tuple(f"%{keyword}%" for keyword in keywords_list)
        rows = self.__execute_query(query, params)
        for row in rows:
            print(row)
