import pytest


@pytest.fixture
def vacancy_for_test_1():
    return {
              'id': '117843032',
              'name': 'Бизнес-партнёр в Финансовую службу',
              'area': {
                'id': '1',
                'name': 'Москва',
                'url': 'https://api.hh.ru/areas/1'
              },
              'salary': None,
              'address': {
                'city': None,
                'metro': None,
              },
              'alternate_url': 'https://hh.ru/vacancy/117843032',
              'employer': {
                'id': '1740',
                'name': 'Яндекс',
                'url': 'https://api.hh.ru/employers/1740',
                'alternate_url': 'https://hh.ru/employer/1740',
                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1740',
              }
            }

@pytest.fixture
def vacancy_for_test_2():
    return {
              'id': '117843032',
              'name': 'Бизнес-партнёр в Финансовую службу',
              'area': {
                'id': '1',
                'name': 'Москва',
                'url': 'https://api.hh.ru/areas/1'
              },
              'salary': {
                  'from': 100000,
              },
              'address': {
                'city': 'Москва',
                'metro': {
                  'station_name': 'Парк культуры',
                  'line_name': 'Сокольническая',
                },
                'raw': 'Ленина 5',
              },
              'alternate_url': 'https://hh.ru/vacancy/117843032',
              'employer': {
                'id': '1740',
                'name': 'Яндекс',
                'url': 'https://api.hh.ru/employers/1740',
                'alternate_url': 'https://hh.ru/employer/1740',
                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1740',
              }
            }
