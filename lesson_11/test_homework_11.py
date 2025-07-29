import pytest
import os

from homework_11 import log_event

log_file = 'login_system.log'

def test_verification_success():

    log_event('Oleh', 'success')

    assert os.path.exists(log_file)

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Oleh' in log_content
    assert 'success' in log_content


def test_verification_expired():

    log_event('Oleh', 'expired')

    assert os.path.exists(log_file)

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Oleh' in log_content
    assert 'expired' in log_content


def test_verification_else():

    log_event('Oleh', '12status')

    assert os.path.exists(log_file)

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Oleh' in log_content
    assert '12status' in log_content

@pytest.mark.parametrize("username, status, expected", [
    ("Oleh", "success", "Status: success"),
    ("Anna", "expired", "Status: expired"),
    ("Ivan", "failed", "Status: failed"),
])

def test_verification(username, status, expected):

    log_event(username, status)

    with open(log_file, 'r') as f:
        content = f.read()

    assert expected in content
    assert f"Username: {username}" in content