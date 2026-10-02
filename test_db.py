import db


def use_temp_db(monkeypatch, tmp_path):
    monkeypatch.setattr(db, "DB_NAME", str(tmp_path / "test.db"))


def test_add_and_get_column(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    db.add_reading("10:00:00", 20.5, 50.0, 500.0)
    db.add_reading("10:00:01", 21.5, 60.0, 600.0)
    assert db.get_column("temperature") == [20.5, 21.5]


def test_count_readings(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    assert db.count_readings() == 0
    db.add_reading("10:00:00", 20.5, 50.0, 500.0)
    assert db.count_readings() == 1


def test_max_temperature_empty_is_none(monkeypatch, tmp_path):
    use_temp_db(monkeypatch, tmp_path)
    assert db.max_temperature() is None