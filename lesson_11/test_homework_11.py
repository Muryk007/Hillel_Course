import pytest
import os

from homework_11 import log_event


def test_verification_success():
    log_file = 'login_system.log'

    log_event('Oleh', 'success')

    assert os.path.exists(log_file)

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Oleh' in log_content
    assert 'success' in log_content


def test_verification_expired():
    log_file = 'login_system.log'

    log_event('Oleh', 'expired')

    assert os.path.exists(log_file)

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Oleh' in log_content
    assert 'expired' in log_content


def test_verification_else():
    log_file = 'login_system.log'

    log_event('Oleh', '12status')

    assert os.path.exists(log_file)

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Oleh' in log_content
    assert '12status' in log_content
