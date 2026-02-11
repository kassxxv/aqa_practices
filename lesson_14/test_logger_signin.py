import pytest
import requests
from lesson_14.homework_14 import log_event

LOG_FILENAME = 'lesson_14/login_system.log'
BASE_URL = 'https://qauto.forstudy.space/api'
USER_CREDENTIALS = {"email": "filip.fylyp07@gmail.com", "password": "5pj7SE53vHsMu5J", "remember": 'false'}
WRONG_USER_CREDENTIALS = {"email": "filip.fylyp07@gmail.com", "password": "WRONG PASSWORD", "remember": 'false'}


def get_log_line_count():
    with open(LOG_FILENAME, 'r') as f:
        return len(f.readlines())


def get_last_log_line():
    with open(LOG_FILENAME, 'r') as f:
        lines = f.readlines()
        return lines[-1]

class TestSigninLogger:
    def test_success_login(self):
        response = requests.post(f'{BASE_URL}/auth/signin', json=USER_CREDENTIALS)
        assert response.status_code == 200

        profile_response = requests.get(f'{BASE_URL}/users/profile', cookies=response.cookies)
        first_name = profile_response.json()['data']['name']

        before = get_log_line_count()
        log_event(first_name, "success")

        assert get_log_line_count() == before + 1, 'Можливо логгер не записав нову інформацію'
        assert f"Username: {first_name}" in get_last_log_line()
        assert "Status: success" in get_last_log_line()

    def test_failed_password(self):
        response = requests.post(f'{BASE_URL}/auth/signin', json=WRONG_USER_CREDENTIALS)
        assert response.status_code == 400

        email = WRONG_USER_CREDENTIALS["email"]
        before = get_log_line_count()
        log_event(email, "failed")

        assert get_log_line_count() == before + 1, 'Можливо логгер не записав нову інформацію'
        assert f"Username: {email}" in get_last_log_line()
        assert "Status: failed" in get_last_log_line()

    def test_expired_password(self):
        user = "ExpiredUser"
        before = get_log_line_count()
        log_event(user, "expired")

        assert get_log_line_count() == before + 1, 'Можливо логгер не записав нову інформацію'
        assert f"Username: {user}" in get_last_log_line()
        assert "Status: expired" in get_last_log_line()
