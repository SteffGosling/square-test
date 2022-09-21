import pytest
import sys


@pytest.fixture(scope="session")  # runs just 1 time and caches the result
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:
        # Connection will be torn down after all tests are run
        yield conn


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1
    monkeypatch.setattr(sys.stdout, "write", fake_write)
    return buffer
