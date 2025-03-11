def type_of_salary_from(vacancy: dict) -> int:
    """Функция, преобразующая зарплату "от" в нужный вид"""
    salary_res = 0
    salary = vacancy.get("salary")
    if isinstance(salary, dict):
        salary_from = salary.get("from")
        if salary_from is not None:
            salary_res = salary_from
    return salary_res


def type_of_salary_to(vacancy: dict) -> int:
    """Функция, преобразующая зарплату "до" в нужный вид"""
    salary_res = 0
    salary = vacancy.get("salary")
    if isinstance(salary, dict):
        salary_to = salary.get("to")
        if salary_to is not None:
            salary_res = salary_to
    return salary_res


def metro_description(vacancy: dict) -> str:
    """Функция обрабатывает информацию по метро"""
    metro_str = "Метро не указано/В этом городе метро нет"
    address = vacancy.get("address")
    if address is not None:
        metro = address.get("metro")
        if metro is not None:
            metro_str = metro.get("station_name", metro_str)
    return metro_str


def city_description(vacancy: dict) -> str:
    """Функция обрабатывает информацию по городу"""
    city_str = "Город не указан"
    address = vacancy.get("address")
    if address is not None:
        city = address.get("city")
        if city is not None:
            city_str = city
    return city_str


def address_description(vacancy: dict) -> str:
    """Функция обрабатывает информацию по адресу"""
    address_str = "Адрес не указан"
    address = vacancy.get("address")
    if address is not None:
        full_address = address.get("raw")
        if full_address is not None:
            address_str = full_address
    return address_str
