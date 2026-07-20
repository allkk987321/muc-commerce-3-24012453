"""第8天 Flask 强化项目测试"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def login(client):
    return client.post("/login", data={"username": "student", "password": "day07"}, follow_redirects=True)


class TestHealthRoute:
    def test_health_returns_json_without_login(self, client):
        resp = client.get("/health")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["ok"] is True
        assert data["service"] == "day08-flask-upgrade"


class TestMetricsAPI:
    def test_metrics_requires_login(self, client):
        resp = client.get("/api/metrics", follow_redirects=True)
        assert "登录" in resp.data.decode("utf-8")

    def test_metrics_returns_four_cards(self, client):
        login(client)
        resp = client.get("/api/metrics")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["ok"] is True
        assert len(data["metrics"]) == 4
        for m in data["metrics"]:
            assert "label" in m
            assert "value" in m
            assert "note" in m


class TestCategoriesAPI:
    def test_categories_all(self, client):
        login(client)
        resp = client.get("/api/categories")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["ok"] is True
        assert data["category"] == "全部"
        assert len(data["rows"]) > 0

    def test_categories_filtered(self, client):
        login(client)
        resp = client.get("/api/categories?category=Fashion")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["category"] == "Fashion"
        for row in data["rows"]:
            assert row["偏好品类"] == "Fashion"


class TestErrorHandling:
    def test_bad_request_returns_json(self, client):
        login(client)
        resp = client.post("/api/ask", json={"question": ""})
        assert resp.status_code == 400
        data = resp.get_json()
        assert data["ok"] is False
        assert len(data["answer"]) > 0
