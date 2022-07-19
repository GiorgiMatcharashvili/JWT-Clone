def shift_right(bits, amount):
    for _ in range(amount):
        bits = '0' + bits[:-1]
    return bits


def rotate_right(bits, amount):
    for _ in range(amount):
        bits = bits[-1] + bits[:-1]
    return bits


def xor(bits):
    while True:
        f, s = bits[:2]
        bits = bits[2:]

        xor_result = ''
        for i, j in zip(f, s):
            xor_result += str(int(i) ^ int(j))
        bits.append(xor_result)

        if len(bits) == 1:
            break
    return bits[0]


def add(bits):
    result = 0
    for each in bits:
        result += int(each, 2)
    result_in_bin = bin(result % (2**32)).replace('0b', '')

    result_in_bin = '0'*(32-len(result_in_bin))+result_in_bin

    return result_in_bin


