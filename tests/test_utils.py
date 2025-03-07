from src.utils import address_description, city_description, metro_description, type_of_salary


def test_type_of_salary_zero(vacancy_for_test_1):
    """Тест на возврат нуля, когда зп не указана"""
    result = type_of_salary(vacancy_for_test_1)
    assert result == 0


def test_type_of_salary_int(vacancy_for_test_2):
    """Тест на корректный возврат зп"""
    result = type_of_salary(vacancy_for_test_2)
    assert result == 100000


def test_metro_description_none(vacancy_for_test_1):
    """Тест на возврат Метро не указано/В этом городе метро нет, когда метро не указано"""
    result = metro_description(vacancy_for_test_1)
    assert result == "Метро не указано/В этом городе метро нет"


def test_metro_description(vacancy_for_test_2):
    """Тест на корректный возврат названия метро"""
    result = metro_description(vacancy_for_test_2)
    assert result == "Парк культуры"


def test_city_description(vacancy_for_test_2):
    """Тест на корректный возврат названия города"""
    result = city_description(vacancy_for_test_2)
    assert result == "Москва"


def test_city_description_none(vacancy_for_test_1):
    """Тест на возврат Город не указан, когда город не указан"""
    result = city_description(vacancy_for_test_1)
    assert result == "Город не указан"


def test_address_description(vacancy_for_test_2):
    """Тест на корректный возврат адреса"""
    result = address_description(vacancy_for_test_2)
    assert result == "Ленина 5"


def test_address_description_none(vacancy_for_test_1):
    """Тест на возврат Адрес не указан, когда адрес не указан"""
    result = address_description(vacancy_for_test_1)
    assert result == "Адрес не указан"
