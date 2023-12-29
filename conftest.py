import pytest
import sys


@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, "write", fake_write)
    return buffer


def test_print(capture_stdout): # capture_stdout is a fixture
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"


@pytest.fixture(scope="session")
def db_conn():
    db = ...  # noqa: F841
    url = ...  # noqa: F841
#   with db.connect(url) as conn:  # connection will be torn down after all tests finish
#       yield conn
