from unittest.mock import Mock

import pytest
from pytest_mock import mocker

from libpythonpro import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/55213845?v=4'
    resp_mock.json.return_value = {
        'login': 'Fabi-Boniolo', 'id': 55213845,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Fabi-Boniolo')
    assert avatar_url == url


def test_buscar_avatar_integraçao():
    url = github_api.buscar_avatar('Fabi-Boniolo')
    assert 'https://avatars.githubusercontent.com/u/55213845?v=4'  == url