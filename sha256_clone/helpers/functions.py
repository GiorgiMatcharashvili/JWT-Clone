from .operations import *


def sigma0(bits):
    return xor([rotate_right(bits, 7), rotate_right(bits, 18), shift_right(bits, 3)])


def sigma1(bits):
    return xor([rotate_right(bits, 17), rotate_right(bits, 19), shift_right(bits, 10)])


def u_sigma0(bits):
    return xor([rotate_right(bits, 2), rotate_right(bits, 13), rotate_right(bits, 22)])


def u_sigma1(bits):
    return xor([rotate_right(bits, 6), rotate_right(bits, 11), rotate_right(bits, 25)])


def choice(bits):
    x, y, z = bits
    result = [z[i] if v == '0' else y[i] for i, v in enumerate(x)]

    return ''.join(result)


def majority(bits):

    result = ['0' if i.count('0') > 1 else '1' for i in zip(*bits)]

    return ''.join(result)
