import pytest

from aoc.day2 import *


@pytest.fixture
def fixture_example():
    return """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


def test_password_freq_simple():
    assert check_password_freq(1, 3, "a", "abcde")
    assert not check_password_freq(1, 3, "b", "cdefg")


def test_parser(fixture_example):
    assert [
        (1, 3, "a", "abcde"),
        (1, 3, "b", "cdefg"),
        (2, 9, "c", "ccccccccc"),
    ] == parse(fixture_example)


def test_problem(fixture_example):
    assert 2 == part1_solve(fixture_example)


def test_password_xor_simple():
    assert check_password_xor(1, 3, "a", "abcde")
    assert not check_password_xor(1, 3, "b", "cdefg")


def test_part2(fixture_example):
    assert 1 == part2_solve(fixture_example)
