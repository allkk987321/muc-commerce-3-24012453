"""Flask 自动化测试 - 拓展任务 C"""
import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pytest
from app import app


@pytest.fixture
def client():
    """创建测试客户端。"""
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test-key"
    with app.test_client() as c:
        yield c


def login(client, username="student", password="day07"):
    """辅助函数：登录并返回响应。"""
    return client.post(
        "/login",
        data={"username": username, "password": password},
        follow_redirects=True,
    )


class TestLogin:
    """登录相关测试"""

    def test_correct_login_redirects_to_dashboard(self, client):
        """测试正确登录后跳转到 /dashboard。"""
        resp = login(client)
        assert resp.status_code == 200
        assert "登录成功" in resp.data.decode("utf-8")

    def test_wrong_password_shows_error(self, client):
        """测试错误密码显示错误信息。"""
        resp = login(client, password="wrong")
        assert resp.status_code == 200
        assert "错误" in resp.data.decode("utf-8")


class TestAccessControl:
    """访问控制测试"""

    def test_unauthenticated_dashboard_redirects_to_login(self, client):
        """测试未登录访问 /dashboard 被拦截。"""
        resp = client.get("/dashboard", follow_redirects=True)
        assert resp.status_code == 200
        assert "登录" in resp.data.decode("utf-8")

    def test_authenticated_dashboard_returns_200(self, client):
        """测试登录后 /dashboard 返回 200。"""
        login(client)
        resp = client.get("/dashboard")
        assert resp.status_code == 200
        assert "数据看板" in resp.data.decode("utf-8")


class TestAPI:
    """API 接口测试"""

    def test_ask_returns_json_when_logged_in(self, client):
        """测试登录后 /api/ask 返回 JSON。"""
        login(client)
        resp = client.post(
            "/api/ask",
            json={"question": "系统中一共有多少用户？"},
        )
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["ok"] is True
        assert len(data["answer"]) > 0

    def test_ask_returns_400_for_empty_question(self, client):
        """测试空问题返回 400。"""
        login(client)
        resp = client.post("/api/ask", json={"question": ""})
        assert resp.status_code == 400


class TestLogout:
    """退出测试"""

    def test_logout_clears_session(self, client):
        """测试退出后访问 /dashboard 被拦截。"""
        login(client)
        client.get("/logout")
        resp = client.get("/dashboard", follow_redirects=True)
        assert "登录" in resp.data.decode("utf-8")
