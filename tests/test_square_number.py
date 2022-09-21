from square.square_number import square_a_number
import pytest


@pytest.mark.parametrize("x, expected", [
    (2, 4),
    (1, 1),
    (1.75, 3.0625),
])
def test_multi_square_a_number(x, expected):
    assert square_a_number(x) == expected


@pytest.mark.skip(reason="This test is not ready yet")
def test_square_a_number_regex():
    assert square_a_number("regex_of_number") == "some_number"


# SkipIf can be used for OS differences


@pytest.mark.xfail
def test_zero_squared():
    assert square_a_number(0) == 0


def test_invalid_input():
    with pytest.raises(TypeError):
        square_a_number("string")


def test_print(capture_stdout):
    print("Hello")
    assert capture_stdout["stdout"] == "Hello\n"
    assert capture_stdout["write_calls"] == 2
