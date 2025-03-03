import requests


class HeadHunterAPI:
    base_url: str
    vacancies_url: str
    vacancies_list: list
    employer_info: dict
    employers_info_list: list

    def __init__(self, url="https://api.hh.ru"):
        """Инициализация класса"""
        self.base_url = url
        self.vacancies_list = []
        self.employer_info = {}
        self.employers_info_list = []

    def get_employer_id_by_name(self, employer_name):
        """Функция для получения id работодателя по названию компании"""
        url = f"{self.base_url}/employers"
        params = {"text": employer_name}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            employers = response.json().get("items", [])
            for employer in employers:
                if employer["name"] == employer_name:
                    self.vacancies_url = employer['vacancies_url']
                    return employer["id"]
            else:
                print(f"Работодатель с названием '{employer_name}' не найден.")
                return None
        else:
            print(f"Ошибка при получении ID работодателя: {response.status_code}")
            return None

    def get_employer_info_by_id(self, employer_id):
        """Функция для получения информации о работодателе по id"""
        response = requests.get(f"{self.base_url}/employers/{employer_id}")
        if response.status_code == 200:
            employer = response.json()
            employer_info = {
                'name': employer["name"],
                'id': employer["id"],
                'vacancies_url': employer['vacancies_url'],
                'site_url': employer['site_url'],
                'description_url': employer['alternate_url']
            }
            return employer_info
        else:
            print(f"Ошибка при получении информации о работодателе: {response.status_code}")
            return None

    def get_employer_vacancies(self):
        """Функция для получения вакансий работодателя по его id"""
        response = requests.get(self.vacancies_url)
        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            print(f"Ошибка при получении вакансий: {response.status_code}")
            return []

    def fetch_vacancies_for_employers(self, employer_names):
        """Получает вакансии для списка работодателей по их названиям."""
        for employer_name in employer_names:
            employer_id = self.get_employer_id_by_name(employer_name)
            if employer_id:
                self.vacancies_list.append(self.get_employer_vacancies())

        return self.vacancies_list

    def fetch_info_for_employers(self, employer_names):
        """Получает информацию о всех работодателях из списка по их названиям."""
        for employer_name in employer_names:
            employer_id = self.get_employer_id_by_name(employer_name)
            if employer_id:
                employer_info = self.get_employer_info_by_id(employer_id)
                if employer_info:
                    self.employers_info_list.append(employer_info)

        return self.employers_info_list

