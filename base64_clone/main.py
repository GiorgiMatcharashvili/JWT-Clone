BASE64_INDEX_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def split_message(message):
    split_amount = 3
    return [message[i:i + split_amount] for i in range(0, len(message), split_amount)]


def translate_letters_in_bits(three_letters):
    bits = ''
    for each_letter in three_letters:
        letter_in_binary = bin(ord(each_letter)).replace("0b", "")

        for i in range(8 - len(letter_in_binary)):
            letter_in_binary = '0' + letter_in_binary

        bits += letter_in_binary
    return bits


def split_in_bits(bits):
    split_amount = 6

    splited_bits = []
    for i in range(0, len(bits), split_amount):
        splited_bit = bits[i:i + split_amount]
        for _ in range(6 - len(splited_bit)):
            splited_bit += '0'

        splited_bits.append(splited_bit)
    return splited_bits


def translate_bit(bit):
    char_index = int(bit, 2)
    return BASE64_INDEX_TABLE[char_index]


def b64encode(s):
    encoded = ''
    splited_message = split_message(s)

    for each_three_letters in splited_message:
        translated_letters = translate_letters_in_bits(each_three_letters)
        splited_bits = split_in_bits(translated_letters)
        for each_bit in splited_bits:
            if each_bit == '=':
                encoded += each_bit
                continue
            encoded += translate_bit(each_bit)
    return encoded


def split_encoded(encoded):
    split_amount = 4
    return [encoded[i:i + split_amount] for i in range(0, len(encoded), split_amount)]


def letters_to_indexes(four_letters):
    indexes = []
    for each in four_letters:
        if each == '=':
            indexes.append('=')
            continue
        indexes.append(BASE64_INDEX_TABLE.index(each))
    return indexes


def indexes_to_bits(indexes):
    bits = ''
    for each in indexes:
        if each == '=':
            bits += each
            continue
        index_in_bits = bin(each).replace("0b", "")
        for i in range(6 - len(index_in_bits)):
            index_in_bits = '0' + index_in_bits
        bits += index_in_bits
    return bits


def split_bits(bits):
    split_amount = 8
    return [bits[i:i + split_amount] for i in range(0, len(bits), split_amount)]


def translate_splited_bits(splited_bits):
    translated_text = ''
    for each in splited_bits:
        if '=' in each:
            continue
        translated_text += chr(int(each, 2))
    return translated_text


def b64decode(s):
    decoded = ''

    splited_encoded = split_encoded(s)

    for each in splited_encoded:
        indexes = letters_to_indexes(each)
        bits = indexes_to_bits(indexes)
        splited_bits = split_bits(bits)
        decoded += translate_splited_bits(splited_bits)

    return decoded
