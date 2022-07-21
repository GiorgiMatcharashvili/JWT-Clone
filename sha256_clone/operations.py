def shift_right(bits, amount):
    for _ in range(amount):
        bits = '0' + bits[:-1]
    return bits


def rotate_right(number, shift):
    return (number >> shift) | (number << 32 - shift)


def sigma0(number):
    number = (rotate_right(number, 7) ^ rotate_right(number, 18) ^ (number >> 3))
    return number


def sigma1(number):
    number = (rotate_right(number, 17) ^ rotate_right(number, 19) ^ (number >> 10))
    return number


def u_sigma0(number):
    number = (rotate_right(number, 2) ^ rotate_right(number, 13) ^ rotate_right(number, 22))
    return number


def u_sigma1(number):
    number = (rotate_right(number, 6) ^ rotate_right(number, 11) ^ rotate_right(number, 25))
    return number


def choice(x, y, z):
    return (x & y) ^ (~x & z)


def majority(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)
