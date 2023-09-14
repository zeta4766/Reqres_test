import random
from string import ascii_letters, digits


def random_number(start: int = 100, end: int = 1000, count = 1) -> list[int]:
    return [random.randint(start, end) for _ in range(count)]


def random_string(start: int = 9, end: int = 15) -> str:
    return ''.join(random.choice(ascii_letters + digits) for _ in range(random.randint(start, end)))


def random_email():
    extension = ['com', 'net', 'org']
    return f"{random_string()}@{random_string(3, 5)}.{random.choice(extension)}"
