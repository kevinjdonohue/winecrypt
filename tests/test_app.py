import falcon
from falcon import testing
import json
import pytest
from winecrypt.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_list_wines(client):
    # arrange
    doc = {
        "wines": [
            {
              "name": "Kevins Fancy Red"
            },
            {
                "name": "Kevins Fancy White"
            }
        ]
    }

    # act
    response = client.simulate_get("/wines")
    # result_doc = msgpack.unpackb(response.content, raw=False)
    result_doc = json.loads(response.content)

    # assert
    assert result_doc == doc
    assert response.status == falcon.HTTP_200
