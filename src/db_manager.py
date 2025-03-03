import psycopg2
from contextlib import closing

class DBManager:
    """Класс для запросов к базе данных"""
    database_name: str
    params: dict

    def __init__(self, database_name: str, params: dict) -> None:
        """Инициализация класса"""
        self.database_name = database_name
        self.params = params

    def connect_to_db(self):
        """Создает соединение с базой данных. Возвращает объект соединения."""
        return psycopg2.connect(dbname=self.database_name, **self.params)

    def execute_query(self, query, params=None):
        """Общий метод для выполнения SQL-запроса"""
        with closing(self.connect_to_db()) as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchall()


    def get_companies_and_vacancies_count(self):
        """Метод для получения списка всех компаний и количества вакансий у каждой компании"""
        query = '''
            SELECT companies.company_name, COUNT(vacancies.vacancy_id)
            FROM companies 
            LEFT JOIN vacancies USING(company_id)
            GROUP BY companies.company_name;
        '''
        rows = self.execute_query(query)
        for row in rows:
            print(row)


    def get_all_vacancies(self):
        """Метод для получения списка всех вакансий с указанием названия компании,
        названия вакансии, зарплаты и ссылки на вакансию"""
        query = '''
            SELECT companies.company_name, vacancies.vacancy_name, vacancies.salary, vacancies.description_url_hh
            FROM vacancies 
            INNER JOIN companies USING(company_id);
        '''
        rows = self.execute_query(query)
        for row in rows:
            print(row)

    def get_avg_salary(self):
        """Метод для получения средней зарплаты по вакансиям"""
        query = '''
            SELECT AVG(salary)
            FROM vacancies 
            WHERE salary > 0;
        '''
        rows = self.execute_query(query)
        for row in rows:
            print(row)

    def get_vacancies_with_higher_salary(self):
        """Метод для получения списка всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        query = '''
            SELECT companies.company_name, vacancies.vacancy_name, vacancies.salary, vacancies.description_url_hh
            FROM vacancies 
            INNER JOIN companies USING(company_id)
            WHERE vacancies.salary > (SELECT AVG(salary) FROM vacancies WHERE salary > 0);
        '''
        rows = self.execute_query(query)
        for row in rows:
            print(row)

    def get_vacancies_with_keyword(self, keyword: str):
        """Метод для получения списка всех вакансий, в названии которых содержатся переданные в метод слова"""
        query = '''
            SELECT companies.company_name, vacancies.vacancy_name, vacancies.salary, vacancies.description_url_hh
            FROM vacancies 
            INNER JOIN companies USING(company_id)
            WHERE vacancies.vacancy_name LIKE %s;
        '''
        rows = self.execute_query(query, ('%' + keyword + '%',))
        for row in rows:
            print(row)