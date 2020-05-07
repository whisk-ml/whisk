import os
import pytest
import json
# import app from the main.py file
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_predict(client):
    # The code below will likely fail when a real model
    # is provided. It should pass on a fresh app.
    response = client.post('/predict',
                            data=json.dumps({"data": [[1]]}),
                            content_type='application/json')
    assert response.status_code == 200
