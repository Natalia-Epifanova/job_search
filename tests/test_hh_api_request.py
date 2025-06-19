from unittest.mock import patch

from src.hh_api_request import HeadHunterAPI


@patch("src.hh_api_request.requests.get")
def test_get_employer_id_by_name(mock_get, employers_hh):
    """Тест корректного ответа по API подключению для get_employer_id_by_name"""
    mock_get.return_value.json.return_value = employers_hh
    mock_get.return_value.status_code = 200
    hh_api_test = HeadHunterAPI()
    emp_id = hh_api_test.get_employer_id_by_name("nails")
    mock_get.assert_called_once()

    assert emp_id == "5912899"


@patch("src.hh_api_request.requests.get")
def test_get_employer_id_by_name_no_such_emp(mock_get, employers_hh):
    """Тест корректного ответа по API подключению, когда работодатель отсутствует в списке"""
    mock_get.return_value.json.return_value = employers_hh
    mock_get.return_value.status_code = 200
    hh_api_test = HeadHunterAPI()
    emp_id = hh_api_test.get_employer_id_by_name("Goog")
    mock_get.assert_called_once()

    assert emp_id is None


@patch("src.hh_api_request.requests.get")
def test_get_employer_id_by_name_no_response(mock_get):
    """Тест ошибки при запросе по API для get_employer_id_by_name"""
    mock_get.return_value.status_code = 400
    hh_api_test = HeadHunterAPI()
    emp_id = hh_api_test.get_employer_id_by_name("nails")
    assert emp_id is None


@patch("src.hh_api_request.requests.get")
def test_get_employer_info_by_id(mock_get, employer_info_in, employer_info_out):
    """Тест корректного ответа по API подключению для get_employer_info"""
    mock_get.return_value.json.return_value = employer_info_in
    mock_get.return_value.status_code = 200
    hh_api_test = HeadHunterAPI()
    emp_info = hh_api_test.get_employer_info_by_id(1455)
    mock_get.assert_called_once()
    assert emp_info == employer_info_out


@patch("src.hh_api_request.requests.get")
def test_get_employer_info_by_id_no_response(mock_get):
    """Тест ошибки при запросе по API для get_employer_info"""
    mock_get.return_value.status_code = 400
    hh_api_test = HeadHunterAPI()
    emp_info = hh_api_test.get_employer_info_by_id(1455)
    assert emp_info is None


@patch("src.hh_api_request.requests.get")
def test_get_employer_vacancies(mock_get, two_vacancies_from_hh_in, two_vacancies_from_hh_out, employers_hh):
    """Тест корректного ответа по API подключению для get_employer_vacancies"""
    mock_get.return_value.json.return_value = employers_hh
    mock_get.return_value.status_code = 200
    hh_api_test = HeadHunterAPI()
    hh_api_test.get_employer_id_by_name("Яндекс")

    mock_get.return_value.json.return_value = two_vacancies_from_hh_in
    mock_get.return_value.status_code = 200
    vacancies = hh_api_test.get_employer_vacancies()

    assert vacancies == two_vacancies_from_hh_out


@patch("src.hh_api_request.requests.get")
def test_get_employer_vacancies_no_emp(mock_get, two_vacancies_from_hh_in, two_vacancies_from_hh_out, employers_hh):
    """Тест корректного ответа по API подключению для get_employer_vacancies, когда работодатель отсутствует"""
    mock_get.return_value.json.return_value = employers_hh
    mock_get.return_value.status_code = 200
    hh_api_test = HeadHunterAPI()
    hh_api_test.get_employer_id_by_name("Goog")

    mock_get.return_value.status_code = 200
    vacancies = hh_api_test.get_employer_vacancies()

    assert vacancies == []


@patch("src.hh_api_request.requests.get")
def test_get_employer_vacancies_no_response(mock_get, employers_hh):
    """Тест ошибки при запросе по API для get_employer_vacancies"""
    mock_get.return_value.json.return_value = employers_hh
    mock_get.return_value.status_code = 200
    hh_api_test = HeadHunterAPI()
    hh_api_test.get_employer_id_by_name("Яндекс")

    mock_get.return_value.status_code = 400
    vacancies = hh_api_test.get_employer_vacancies()
    assert vacancies == []
