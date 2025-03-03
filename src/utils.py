def type_of_salary(vacancy: dict) -> int:
    """Функция, преобразующая зарплату в нужный вид"""
    salary_res = 0
    salary = vacancy.get("salary")
    if isinstance(salary, dict):
        salary_from = salary.get("from")
        if salary_from is not None:
            salary_res = salary_from
    return salary_res


def metro_description(vacancy: dict) -> str:
    """Функция обрабатывает информацию по метро"""
    metro_str = "Метро не указано/В этом городе метро нет"  # значение по умолчанию
    address = vacancy.get("address")
    if address is not None:
        metro = address.get("metro")
        if metro is not None:
            metro_str = metro.get("station_name", metro_str)
    return metro_str


def city_description(vacancy: dict) -> str:
    """Функция обрабатывает информацию по городу"""
    city_str = "Город не указан"  # значение по умолчанию
    address = vacancy.get("address")
    if address is not None:
        city_str = address.get("city", city_str)
    return city_str


def address_description(vacancy: dict) -> str:
    """Функция обрабатывает информацию по адресу"""
    address_str = "Адрес не указан"  # значение по умолчанию
    address = vacancy.get("address")
    if address is not None:
        address_str = address.get("raw", address_str)
    return address_str
