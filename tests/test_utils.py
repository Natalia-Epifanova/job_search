from src.utils import type_of_salary, metro_description, city_description, address_description


def test_type_of_salary_zero(vacancy_for_test_1):
    result = type_of_salary(vacancy_for_test_1)
    assert result == 0

def test_type_of_salary_int(vacancy_for_test_2):
    result = type_of_salary(vacancy_for_test_2)
    assert result == 100000

def test_metro_description_none(vacancy_for_test_1):
    result = metro_description(vacancy_for_test_1)
    assert result == 'Метро не указано/В этом городе метро нет'

def test_metro_description(vacancy_for_test_2):
    result = metro_description(vacancy_for_test_2)
    assert result == 'Парк культуры'

def test_city_description(vacancy_for_test_2):
    result = city_description(vacancy_for_test_2)
    assert result == "Москва"

def test_city_description_none(vacancy_for_test_1):
    result = city_description(vacancy_for_test_1)
    assert result == "Город не указан"

def test_address_description(vacancy_for_test_2):
    result = address_description(vacancy_for_test_2)
    assert result == "Ленина 5"

def test_address_description_none(vacancy_for_test_1):
    result = address_description(vacancy_for_test_1)
    assert result == "Адрес не указан"

