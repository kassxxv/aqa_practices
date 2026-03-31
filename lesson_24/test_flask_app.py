import pytest
import requests
from requests.auth import HTTPBasicAuth
from logger import logger

BASE_URL = 'http://127.0.0.1:8080'

@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    response = session.post(f'{BASE_URL}/auth', auth=HTTPBasicAuth('test_user', 'test_pass'))
    assert response.status_code == 200, f'Авторизація провалилась: {response.text}'

    access_token = response.json()['access_token']
    session.headers.update({'Authorization': 'Bearer ' + access_token})
    logger.info('Auth: сессія створена і токен JWT повернений')
    yield session

    session.close()
    logger.info('Auth: сессія закрита')


@pytest.mark.parametrize('sort_by, limit', [('price', 5), ('year', 3), ('engine_volume', 7),
    ('brand', 10), (None, 5), ('price', None), (None, None),])
class TestCarSearch:
    def test_get_cars(self, auth_session, sort_by, limit):
        params = {}
        if sort_by is not None:
            params['sort_by'] = sort_by
        if limit is not None:
            params['limit'] = limit

        logger.info(f'GET /cars з параметрами: sort_by={sort_by}, limit={limit}')
        response = auth_session.get(f'{BASE_URL}/cars', params=params)

        logger.info(f'Response status: {response.status_code}')
        logger.debug(f'Response body: {response.json()}')

        assert response.status_code == 200
        cars = response.json()
        assert isinstance(cars, list), 'Відповідь має бути списком'

        if limit is not None:
            assert len(cars) <= limit, f'Очікується менше {limit} машин, отримали {len(cars)}'

        logger.info(f'PASSED: отримано {len(cars)} машин, sort_by={sort_by}, limit={limit}')
