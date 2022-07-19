import math
from .helpers import *

C = []


def constants():
    prime = 2
    while len(C) < 64:
        formatted = round(float(format(math.pow(prime, 1 / 3), '.18g')) % 1, 17)
        formatted *= 2 ** 32
        formatted = int(formatted)
        in_bits = bin(formatted).replace('0b', "")
        in_bits = '0' * (32 - len(in_bits)) + in_bits
        C.append(in_bits)

        # Find next prime number
        number = prime
        while True:
            number += 1
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                prime = number
                break


def initial_hash_values():
    values = []
    prime = 2
    for _ in range(8):
        formatted = int(round(float(format(math.pow(prime, 1 / 2), '.12g')) % 1, 11) * 2 ** 32)
        in_bits = bin(formatted).replace('0b', "")
        in_bits = '0' * (32 - len(in_bits)) + in_bits
        values.append(in_bits)

        # Find next prime number
        number = prime
        while True:
            number += 1
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                prime = number
                break
    return values


def message(msg):
    result = ''
    for i in msg:
        each_in_bin = bin(ord(i)).replace('0b', '')
        each_in_bin = '0' * (8 - len(each_in_bin)) + each_in_bin
        result += each_in_bin
    return result


def padding(msg_bits):
    msg_len = bin(len(msg_bits)).replace('0b', '')
    msg_len = '0' * (64 - len(msg_len)) + msg_len

    msg_bits += '1'
    while (len(msg_bits) + 64) % 512 != 0:
        msg_bits += '0'

    msg_bits += msg_len

    return msg_bits


def message_blocks(padded_bits):
    return [padded_bits[i:i + 512] for i in range(0, len(padded_bits), 512)]


def message_schedule(blocks):
    schedules = []
    for message_blk in blocks:
        schedule = [message_blk[i:i + 32] for i in range(0, len(message_blk), 32)]
        for _ in range(64 - len(schedule)):
            i = len(schedule)
            new = add([sigma1(schedule[i - 2]), schedule[i - 7], sigma0(schedule[i - 15]), schedule[i - 16]])
            schedule.append(new)
        schedules.append(schedule)
    return schedules


def compression(schedules):
    I = initial_hash_values()
    a, b, c, d, e, f, g, h = initial_hash_values()
    constants()

    for schedule in schedules:
        for word, constant in zip(schedule, C):
            t1 = add([u_sigma1(e), choice([e, f, g]), h, constant, word])
            t2 = add([u_sigma0(a), majority([a, b, c])])

            a, b, c, d, e, f, g, h = add([t1, t2]), a, b, c, d, e, f, g

            e = add([e, t1])

        a = add([a, I[0]])
        b = add([b, I[1]])
        c = add([c, I[2]])
        d = add([d, I[3]])
        e = add([e, I[4]])
        f = add([f, I[5]])
        g = add([g, I[6]])
        h = add([h, I[7]])

        I = [a, b, c, d, e, f, g, h]

    return ''.join([hex(int(i, 2)).replace('0x', '') for i in I])


def generate_hash(text):
    msg = message(text)
    padded = padding(msg)
    msg_blk = message_blocks(padded)
    msg_sch = message_schedule(msg_blk)
    compressed = compression(msg_sch)
    return compressed
