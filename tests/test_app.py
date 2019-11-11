import falcon
from falcon import testing
import msgpack
import pytest
from winecrypt.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_list_wines(client):
    doc = {
        "wines": [
          {
              "name": "Some Fancy Wine"
          }
        ]
    }

    response = client.simulate_get("/wines")

    result_doc = msgpack.unpackb(response.content, raw=False)

    assert result_doc == doc
    assert response.status == falcon.HTTP_200
