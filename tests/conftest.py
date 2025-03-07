import pytest


@pytest.fixture
def vacancy_for_test_1():
    return {
        "id": "117843032",
        "name": "Бизнес-партнёр в Финансовую службу",
        "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
        "salary": None,
        "address": {
            "city": None,
            "metro": None,
        },
        "alternate_url": "https://hh.ru/vacancy/117843032",
        "employer": {
            "id": "1740",
            "name": "Яндекс",
            "url": "https://api.hh.ru/employers/1740",
            "alternate_url": "https://hh.ru/employer/1740",
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1740",
        },
    }


@pytest.fixture
def vacancy_for_test_2():
    return {
        "id": "117843032",
        "name": "Бизнес-партнёр в Финансовую службу",
        "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
        "salary": {
            "from": 100000,
        },
        "address": {
            "city": "Москва",
            "metro": {
                "station_name": "Парк культуры",
                "line_name": "Сокольническая",
            },
            "raw": "Ленина 5",
        },
        "alternate_url": "https://hh.ru/vacancy/117843032",
        "employer": {
            "id": "1740",
            "name": "Яндекс",
            "url": "https://api.hh.ru/employers/1740",
            "alternate_url": "https://hh.ru/employer/1740",
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1740",
        },
    }


@pytest.fixture()
def employers_hh():
    return {
        "items": [
            {
                "id": "5912899",
                "name": "nails",
                "url": "https://api.hh.ru/employers/5912899",
                "alternate_url": "https://hh.ru/employer/5912899",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5912899",
            },
            {
                "id": "1740",
                "name": "Яндекс",
                "url": "https://api.hh.ru/employers/1740",
                "alternate_url": "https://hh.ru/employer/1740",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1740",
            },
        ],
        "found": 2224227,
        "pages": 111212,
        "page": 0,
        "per_page": 20,
    }


@pytest.fixture()
def employer_info_in():
    return {
        "alternate_url": "https://hh.ru/employer/1455",
        "area": {"id": "113", "name": "Россия", "url": "https://api.hh.ru/areas/113"},
        "description": "Хороший работодатель",
        "id": "1455",
        "name": "HeadHunter",
        "open_vacancies": 19,
        "site_url": "https://hh.ru",
        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1455",
    }


@pytest.fixture()
def employer_info_out():
    return {
        "name": "HeadHunter",
        "id": "1455",
        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1455",
        "site_url": "https://hh.ru",
        "description_url": "https://hh.ru/employer/1455",
    }


@pytest.fixture()
def two_vacancies_from_hh_in():
    return {
        "items": [
            {
                "id": "117843032",
                "name": "Бизнес-партнёр в Финансовую службу",
                "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
                "salary": None,
                "address": {
                    "city": None,
                    "metro": None,
                },
                "alternate_url": "https://hh.ru/vacancy/117843032",
                "employer": {
                    "id": "1740",
                    "name": "Яндекс",
                    "url": "https://api.hh.ru/employers/1740",
                    "alternate_url": "https://hh.ru/employer/1740",
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1740",
                },
            },
            {
                "id": "117843032",
                "name": "Бизнес-партнёр в Финансовую службу",
                "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
                "salary": {
                    "from": 100000,
                },
                "address": {
                    "city": "Москва",
                    "metro": {
                        "station_name": "Парк культуры",
                        "line_name": "Сокольническая",
                    },
                    "raw": "Ленина 5",
                },
                "alternate_url": "https://hh.ru/vacancy/117843032",
                "employer": {
                    "id": "1740",
                    "name": "Яндекс",
                    "url": "https://api.hh.ru/employers/1740",
                    "alternate_url": "https://hh.ru/employer/1740",
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1740",
                },
            },
        ],
        "pages": 64,
        "page": 0,
    }


@pytest.fixture()
def two_vacancies_from_hh_out():
    return [
        {
            "id": "117843032",
            "name": "Бизнес-партнёр в Финансовую службу",
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": None,
            "address": {
                "city": None,
                "metro": None,
            },
            "alternate_url": "https://hh.ru/vacancy/117843032",
            "employer": {
                "id": "1740",
                "name": "Яндекс",
                "url": "https://api.hh.ru/employers/1740",
                "alternate_url": "https://hh.ru/employer/1740",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1740",
            },
        },
        {
            "id": "117843032",
            "name": "Бизнес-партнёр в Финансовую службу",
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {
                "from": 100000,
            },
            "address": {
                "city": "Москва",
                "metro": {
                    "station_name": "Парк культуры",
                    "line_name": "Сокольническая",
                },
                "raw": "Ленина 5",
            },
            "alternate_url": "https://hh.ru/vacancy/117843032",
            "employer": {
                "id": "1740",
                "name": "Яндекс",
                "url": "https://api.hh.ru/employers/1740",
                "alternate_url": "https://hh.ru/employer/1740",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1740",
            },
        },
    ]


@pytest.fixture()
def two_employers_vacancies_in():
    return {
        "items": [
            {
                "id": "116524223",
                "name": "Модератор в команду модерации ВКонтакте",
                "salary": None,
                "address": None,
                "published_at": "2025-02-25T16:26:34+0300",
                "alternate_url": "https://hh.ru/vacancy/116524223",
                "employer": {
                    "id": "15478",
                    "name": "VK",
                    "url": "https://api.hh.ru/employers/15478",
                    "alternate_url": "https://hh.ru/employer/15478",
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=15478",
                },
            },
            {
                "id": "116857792",
                "premium": False,
                "name": "AppSec инженер",
                "salary": None,
                "address": {
                    "city": "Москва",
                    "raw": "Москва, улица Годовикова, 9с10",
                    "metro": {
                        "station_name": "Алексеевская",
                        "line_name": "Калужско-Рижская",
                    },
                    "published_at": "2025-02-24T16:32:37+0300",
                    "alternate_url": "https://hh.ru/vacancy/116857792",
                    "employer": {
                        "id": "1455",
                        "name": "HeadHunter",
                        "url": "https://api.hh.ru/employers/1455",
                        "alternate_url": "https://hh.ru/employer/1455",
                        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1455",
                    },
                },
            },
        ]
    }


@pytest.fixture()
def two_employers_vacancies_out():
    return [
        [
            {
                "id": "116524223",
                "name": "Модератор в команду модерации ВКонтакте",
                "salary": None,
                "address": None,
                "published_at": "2025-02-25T16:26:34+0300",
                "alternate_url": "https://hh.ru/vacancy/116524223",
                "employer": {
                    "id": "15478",
                    "name": "VK",
                    "url": "https://api.hh.ru/employers/15478",
                    "alternate_url": "https://hh.ru/employer/15478",
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=15478",
                },
            },
            {
                "id": "116857792",
                "premium": False,
                "name": "AppSec инженер",
                "salary": None,
                "address": {
                    "city": "Москва",
                    "raw": "Москва, улица Годовикова, 9с10",
                    "metro": {
                        "station_name": "Алексеевская",
                        "line_name": "Калужско-Рижская",
                    },
                    "published_at": "2025-02-24T16:32:37+0300",
                    "alternate_url": "https://hh.ru/vacancy/116857792",
                    "employer": {
                        "id": "1455",
                        "name": "HeadHunter",
                        "url": "https://api.hh.ru/employers/1455",
                        "alternate_url": "https://hh.ru/employer/1455",
                        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1455",
                    },
                },
            },
        ]
    ]


@pytest.fixture()
def employers_hh_2():
    return {
        "items": [
            {
                "id": "15478",
                "name": "HeadHunter",
                "url": "https://api.hh.ru/employers/15478",
                "alternate_url": "https://hh.ru/employer/15478",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=15478",
            },
            {
                "id": "1740",
                "name": "VK",
                "url": "https://api.hh.ru/employers/1740",
                "alternate_url": "https://hh.ru/employer/1740",
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1740",
            },
        ]
    }
