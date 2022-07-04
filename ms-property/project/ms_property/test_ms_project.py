import pytest

from . import server
from requests import Session as RequestsSession
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter


class APITest(server.API):
    def test(self, base_url='http://mockserver'):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session


@pytest.fixture
def api():
    return APITest()


@pytest.fixture
def client(api):
    return api.test()


def test_properties_endpoint(api, client):
    res = client.get('http://mockserver/properties')
    assert res.status_code == 200

def test_properties_endpoint_with_limit(api, client):
    limit = 5
    res = client.get(f'http://mockserver/properties?limit={limit}')
    assert res.status_code == 200
    assert len(res.json()) == limit

