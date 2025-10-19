import pytest

from decorators import log


@log()
def add(x, y):
    return x + y


@log()
def fail_func():
    raise ValueError("oops")


def test_add(capsys):
    assert add(2, 3) == 5
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_fail_func(capsys):
    with pytest.raises(ValueError):
        fail_func()
    captured = capsys.readouterr()
    assert "fail_func error: ValueError" in captured.out
