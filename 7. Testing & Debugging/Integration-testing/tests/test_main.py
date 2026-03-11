from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app=app)


def test_eligibity_pass():
    payload = {
        'income':60000,
        'age':25,
        'employement_status':'employed'
    }

    response = client.post("/loan_eligibility",json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligibility':True}


def test_eligibity_fail():

    payload = {
        'income':40000,
        'age':18,
        'employement_status':'unemployed'
    }

    response = client.post("/loan_eligibility",json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligibility':False}




