from contextlib import closing
from typing import Any, Dict, List

import psycopg2

from src.utils import address_description, city_description, metro_description, type_of_salary


# class CreateDB:
#     """Класс для создания и заполнения базы данных"""
#     database_name: str
#     params: dict
#
#     def __init__(self, database_name: str, params: dict) -> None:
#         """Инициализация класса"""
#         self.database_name = database_name
#         self.params = params
#
#     def connect_to_db(self):
#         """Создает соединение с базой данных. Возвращает объект соединения."""
#         return psycopg2.connect(dbname=self.database_name, **self.params)
#
#     def execute_query(self, query, params=None):
#         """Общий метод для выполнения SQL-запроса"""
#         with closing(self.connect_to_db()) as conn:
#             with conn.cursor() as cur:
#                 cur.execute(query, params)
#
#
#     def create_database(self) -> None:
#         """Метод для создания базы данных"""
#         conn = psycopg2.connect(dbname="postgres", **self.params)
#         conn.autocommit = True
#         cur = conn.cursor()
#         try:
#                 cur.execute(f"DROP DATABASE IF EXISTS {self.database_name}")
#                 cur.execute(f"CREATE DATABASE {self.database_name}")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#         finally:
#             cur.close()
#             conn.close()
#         # try:
#         #     query = f'''
#         #             DROP DATABASE IF EXISTS {self.database_name};
#         #             CREATE DATABASE {self.database_name}
#         #         '''
#         #     self.execute_query(query)
#         # except Exception as e:
#         #     print(f"An error occurred: {e}")
#
#     def create_tables_in_the_database(self) -> None:
#         """Метод для создания таблиц в базе данных"""
#         try:
#             query = '''
#                 CREATE TABLE IF NOT EXISTS companies (
#                         company_id SERIAL PRIMARY KEY,
#                         company_name VARCHAR(50) NOT NULL UNIQUE,
#                         id_hh INT NOT NULL,
#                         description_url_hh TEXT,
#                         site_url TEXT,
#                         vacancies_url TEXT);
#                 CREATE TABLE IF NOT EXISTS vacancies (
#                         vacancy_id SERIAL PRIMARY KEY,
#                         company_id INT REFERENCES companies(company_id),
#                         vacancy_name VARCHAR(255) NOT NULL,
#                         salary INT,
#                         city VARCHAR(50),
#                         metro_station VARCHAR(50),
#                         address VARCHAR(255),
#                         description_url_hh TEXT,
#                         publish_date DATE)
#                 '''
#             self.execute_query(query)
#         except Exception as e:
#             print(f"Произошла ошибка при создании таблиц: {e}")
#
#     def save_companies_in_tables(self, companies: List[Dict[str, Any]]) -> Dict[str, Any]:
#         """Метод для заполнения таблицы с информацией о компаниях"""
#         company_id_map = {}
#         try:
#             query ='''
#                         INSERT INTO companies (company_name, id_hh, description_url_hh, site_url, vacancies_url)
#                         VALUES (%s, %s, %s, %s, %s)
#                         RETURNING company_id,
#                         ,
#                         (
#                             company["name"],
#                             company["id"],
#                             company["description_url"],
#                             company["site_url"],
#                             company["vacancies_url"],
#                             ),'''
#             company_id = cur.fetchone()[0]
#             company_id_map[company["name"]] = company_id
        

def create_database(database_name: str, params: dict) -> None:
    """Функция создает базу данных"""
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
        cur.execute(f"CREATE DATABASE {database_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()


def create_tables_in_the_database(database_name: str, params: dict) -> None:
    """Функция создает таблицы в базе данных"""
    with psycopg2.connect(dbname=database_name, **params) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS companies (
                        company_id SERIAL PRIMARY KEY,
                        company_name VARCHAR(50) NOT NULL UNIQUE,
                        id_hh INT NOT NULL,
                        description_url_hh TEXT,
                        site_url TEXT,
                        vacancies_url TEXT)
                    """
                )

                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS vacancies (
                        vacancy_id SERIAL PRIMARY KEY,
                        company_id INT REFERENCES companies(company_id),
                        vacancy_name VARCHAR(255) NOT NULL,
                        salary INT,
                        city VARCHAR(50),
                        metro_station VARCHAR(50),
                        address VARCHAR(255),
                        description_url_hh TEXT,
                        publish_date DATE)
                    """
                )
            except Exception as e:
                print(f"Произошла ошибка при создании таблиц: {e}")
    conn.close()


def save_companies_in_tables(companies: List[Dict[str, Any]], database_name: str, params: dict) -> Dict[str, Any]:
    """Функция заполняет таблицу с информацией о компаниях"""
    company_id_map = {}
    with psycopg2.connect(dbname=database_name, **params) as conn:
        with conn.cursor() as cur:
            for company in companies:
                cur.execute(
                    """
                INSERT INTO companies (company_name, id_hh, description_url_hh, site_url, vacancies_url)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING company_id
                """,
                (
                    company["name"],
                    company["id"],
                    company["description_url"],
                    company["site_url"],
                    company["vacancies_url"],
                    ),
                )
                company_id = cur.fetchone()[0]
                company_id_map[company["name"]] = company_id
    conn.close()
    return company_id_map



def save_vacancies_in_tables(
    vacancies: List[List[Dict[str, Any]]], company_id_map: Dict[str, Any], database_name: str, params: dict
) -> None:
    """Функция заполняет таблицу с информацией о вакансиях"""
    with psycopg2.connect(dbname=database_name, **params) as conn:
        with conn.cursor() as cur:
            for el in vacancies:
                for vacancy in el:
                    company_name = vacancy["employer"]["name"]
                    company_id = company_id_map.get(company_name)
                    if company_id is not None:
                        cur.execute(
                            """
                            INSERT INTO vacancies (company_id, vacancy_name, salary, city, metro_station,
                            address, description_url_hh, publish_date)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                            """,
                            (
                                company_id,
                                vacancy["name"],
                                type_of_salary(vacancy),
                                city_description(vacancy),
                                metro_description(vacancy),
                                address_description(vacancy),
                                vacancy["alternate_url"],
                                vacancy["published_at"],
                            ),
                        )
    conn.close()
