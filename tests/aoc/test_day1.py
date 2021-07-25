import pytest

from aoc.day1 import parser, find_target, part1_solve, part2_solve


@pytest.fixture
def fixture_example():
    return """1721
979
366
299
675
1456
"""


def test_parser(fixture_example):
    assert parser("1721\n979\n") == [1721, 979]


def test_target_pairs(fixture_example):
    example = parser(fixture_example)
    pair = find_target(2020, example)
    assert set(pair) == {1721, 299}


def test_target_pairs_empty():
    pair = find_target(2020, [])
    assert pair is None


def test_problem(fixture_example):
    assert 514579 == part1_solve(fixture_example)


def test_part2(fixture_example):
    assert 241861950 == part2_solve(fixture_example)
