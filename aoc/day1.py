import itertools


def parser(text_blob):
    return [int(x) for x in text_blob.split()]


def find_target(target, expenses, count=2):
    combs = itertools.combinations(expenses, count)
    target_pair = next(filter(lambda x: sum(x) == target, combs), None)
    return target_pair


def part1_solve(text_blob):
    data = parser(text_blob)
    (x, y) = find_target(2020, data)
    return x * y


def part2_solve(text_blob):
    data = parser(text_blob)
    (x, y, z) = find_target(2020, data, 3)
    return x * y * z
