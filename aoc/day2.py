import re


def parse(text_blob):
    p = re.compile("(\\d+)-(\\d+) (\\w): (\\w+)\n")

    def parse_match(m):
        (n1, n2, c, pw) = m.groups()
        return (int(n1), int(n2), c, pw)

    return [parse_match(m) for m in p.finditer(text_blob)]


def check_password_freq(min_n, max_n, char, password):
    count = password.count(char)
    return count >= min_n and count <= max_n


def solve(text_blob, f):
    data = parse(text_blob)
    return len([1 for m in data if f(*m)])


def part1_solve(text_blob):
    return solve(text_blob, check_password_freq)


def check_password_xor(p1, p2, char, password):
    return (password[p1 - 1] == char) != (password[p2 - 1] == char)


def part2_solve(text_blob):
    return solve(text_blob, check_password_xor)
