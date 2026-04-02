import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_service_name(client):
    response = client.get("/")
    data = response.get_json()
    assert data["service"] == "secure-delivery-platform"


def test_health_returns_healthy(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_health_has_timestamp(client):
    response = client.get("/health")
    data = response.get_json()
    assert "timestamp" in data