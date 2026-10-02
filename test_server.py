import db
import server
from fastapi.testclient import TestClient

client = TestClient(server.app)

SAMPLE = {"time": "10:00:00", "temperature": 20.5, "humidity": 50.0, "co2": 500.0}


def use_temp_db(monkeypatch, tmp_path):
    monkeypatch.setattr(db, "DB_NAME", str(tmp_path / "test.db"))


def test_post_reading_saves(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    response = client.post("/readings", json=SAMPLE)
    assert response.status_code == 200
    assert response.json() == {"status": "saved"}


def test_get_empty_database(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    response = client.get("/readings")
    assert response.json() == {"count": 0}


def test_get_after_posts(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    client.post("/readings", json=SAMPLE)
    client.post("/readings", json={**SAMPLE, "temperature": 25.0})
    response = client.get("/readings")
    assert response.json() == {"count": 2, "latest_temperature": 25.0}


def test_bad_temperature_is_rejected(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    response = client.post("/readings", json={**SAMPLE, "temperature": "hot"})
    assert response.status_code == 422


def test_max_temperature(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    client.post("/readings", json=SAMPLE)
    client.post("/readings", json={**SAMPLE, "temperature": 25.0})
    response = client.get("/readings/max")
    assert response.json() == {"max_temperature": 25.0}


def test_latest_returns_newest_first(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    client.post("/readings", json=SAMPLE)
    client.post("/readings", json={**SAMPLE, "temperature": 25.0})
    response = client.get("/readings/latest?limit=1")
    assert len(response.json()) == 1
    assert response.json()[0]["temperature"] == 25.0

def test_min_temperature(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    client.post("/readings", json=SAMPLE)
    client.post("/readings", json={**SAMPLE, "temperature": 18.0})
    response = client.get("/readings/min")
    assert response.json() == {"min_temperature": 18.0}