import pytest
import requests
import logging.config

from pathlib import Path
from lesson_24.app import users

log_file = Path(__file__).parent / "test_search.log"

config = {
    "version": 1,
    "formatters": {"default": {"format": "%(asctime)s - %(levelname)s - %(message)s"}},
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "default"},
        "file": {"class": "logging.FileHandler", "formatter": "default", "filename": str(log_file), "mode": "w"}
    },
    "loggers": {
        "test_logger": {"handlers": ["console", "file"], "level": "INFO"}
    }
}

logging.config.dictConfig(config)
logger = logging.getLogger("test_logger")

@pytest.fixture(scope="class")
def base_url():
    print("Викликаємо фікстуру base_url")
    return "http://127.0.0.1:8080"

@pytest.mark.parametrize("username, password", list(users.items()))
def test_auth_positive(base_url, username, password):
    # крок 1: отримуємо токен
    auth_resp = requests.post(f"{base_url}/auth", auth=(username, password))
    assert auth_resp.status_code == 200
    data = auth_resp.json()
    assert "access_token" in data
    logger.info(f"Успішна авторизація для користувача: {username}")

negative_users = {
    "test_user": "password",
    "user": "test_pass",
    "admin": "admin",
}
@pytest.mark.parametrize("username, password", list(negative_users.items()))
def test_auth_negative(base_url, username, password):
    auth_resp = requests.post(f"{base_url}/auth", auth=(username, password))
    assert auth_resp.status_code == 401
    assert auth_resp.json()["message"] == "Неправильне ім'я користувача або пароль!"
    logger.info(f"Невдала авторизація для користувача: {username}")

@pytest.fixture(scope="class")
def auth_token(base_url):
    resp = requests.post(f"{base_url}/auth", auth=("test_user", "test_pass"))
    assert resp.status_code == 200
    return resp.json()["access_token"]

@pytest.mark.parametrize(
    "sort_by, limit",
    [
        (None, None),
        ("brand", None),
        ("year", None),
        ("price", None),
        ("engine_volume", 5),
        ("brand", 10),
        ("year", 3)
    ]
)
def test_cars_search(base_url, auth_token, sort_by, limit):
    """Тест GET /cars з різними параметрами sort_by та limit"""
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    headers = {"Authorization": f"Bearer {auth_token}"}
    resp = requests.get(f"{base_url}/cars", headers=headers, params=params)
    assert resp.status_code == 200, f"Помилка запиту: {resp.text}"

    data = resp.json()
    assert isinstance(data, list), "Очікуємо список автомобілів"
    if limit:
        assert len(data) <= limit, f"Очікувано <= {limit}, отримано {len(data)}"

    logger.info(f"Тест пройдено для sort_by={sort_by}, limit={limit}, отримано {len(data)} автомобілів")