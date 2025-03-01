import requests


class HeadHunterAPI:
    base_url: str
    vacancies_url: str

    def __init__(self, url="https://api.hh.ru"):
        """Инициализация класса"""
        self.base_url = url

    def get_employer_id_by_name(self, employer_name):
        """Функция для получения id работодателя по названию компании и получения ссылки на вакансии"""
        url = f"{self.base_url}/employers"
        params = {"text": employer_name}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            employers = response.json().get("items", [])
            for employer in employers:
                if employer["name"] == employer_name:
                    self.vacancies_url = employer["vacancies_url"]
                    return employer["id"]
            else:
                print(f"Работодатель с названием '{employer_name}' не найден.")
                return None
        else:
            print(f"Ошибка при получении ID работодателя: {response.status_code}")
            return None

    def get_employer_vacancies(self):
        """Функция для получения вакансий работодателя по его id"""
        response = requests.get(self.vacancies_url)
        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            print(f"Ошибка при получении вакансий: {response.status_code}")
            return []

    #
    #     if response.status_code == 200:
    #         return response.json().get('items', [])

    #
    # def fetch_vacancies_for_employers(self, employer_names):
    #     """Получает вакансии для списка работодателей по их названиям."""
    #     for employer_name in employer_names:
    #         employer_id = self.get_employer_id(employer_name)
    #         if employer_id:
    #             vacancies = self.get_employer_vacancies(employer_id)
    #             print(f"Вакансии для работодателя '{employer_name}':")
    #             for vac in vacancies:
    #                 salary = vac.get('salary', {})
    #                 salary_from = salary.get('from', 'не указана')
    #                 salary_to = salary.get('to', 'не указана')
    #                 print(f"- {vac['name']} (Зарплата: {salary_from} - {salary_to})")
    #             print("\n")  # Пустая строка для разделения между работодателями


# if __name__ == "__main__":
#     # Список названий работодателей, от которых вы хотите получать данные о вакансиях
#     employer_names = [
#         "Яндекс",
#         "Сбер",
#         "Тинькофф",
#         "Mail.ru Group",
#         "Газпром",
#         "РТС",
#         "Альфа-Банк",
#         "Ростелеком",
#         "МТС",
#         "ВТБ"
#     ]
#
#     hh_api = HeadHunterAPI()
#     hh_api.get_employer_id_by_name('Ростелеком')
#     print(hh_api.get_employer_vacancies())
#  #   hh_api.fetch_vacancies_for_employers(employer_names)
