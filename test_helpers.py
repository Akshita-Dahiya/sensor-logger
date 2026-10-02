import pytest
from helpers import load_column


def make_sample_csv(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(
        "time,temperature,humidity,co2\n"
        "10:00:00,20.5,50.0,500.0\n"
        "10:00:01,21.5,60.0,600.0\n"
    )
    return str(csv_file)


def test_load_temperature(tmp_path):
    filename = make_sample_csv(tmp_path)
    result = load_column(filename, "temperature")
    assert result == [20.5, 21.5]


def test_load_humidity(tmp_path):
    filename = make_sample_csv(tmp_path)
    result = load_column(filename, "humidity")
    assert result == [50.0, 60.0]


def test_missing_column_raises_error(tmp_path):
    filename = make_sample_csv(tmp_path)
    with pytest.raises(KeyError):
        load_column(filename, "pressure")