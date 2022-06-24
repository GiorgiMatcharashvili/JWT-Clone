from base64_clone.main import *
import unittest


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.split_message = "1234567"
        self.splited_message = ["123", "456", "7"]

        self.three_letters = 'ld'
        self.translated_letters = '0110110001100100'

        self.bits = '0110110001100100'
        self.splited_bits = ['011011', '000110', '010000', '=']

        self.bit = '11010'
        self.translated_bit = 'a'

        self.message = 'hello world'
        self.encoded_message = 'aGVsbG8gd29ybGQ='

        self.encoded = 'aGVsbG8gd29ybGQ='
        self.splited_encoded = ["aGVs", "bG8g", "d29y", "bGQ="]

        self.four_letters = 'bGQ='
        self.indexes = [27, 6, 16, '=']

        self.bits_decode = '011011000110010000='

        self.splited_bits_decode = ['01101100', '01100100', '00=']

        self.translated_bits_decode = 'ld'

        self.message_for_all = "some ^text& :"

    def test__split_message(self):
        response = split_message(self.split_message)
        self.assertEqual(response, self.splited_message)

    def test__translate_letters_in_bits(self):
        response = translate_letters_in_bits(self.three_letters)
        self.assertEqual(response, self.translated_letters)

    def test__split_in_bits(self):
        response = split_in_bits(self.bits)
        self.assertEqual(response, self.splited_bits)

    def test__translate_bit(self):
        response = translate_bit(self.bit)
        self.assertEqual(response, self.translated_bit)

    def test__b64encode(self):
        response = b64encode(self.message)
        self.assertEqual(response, self.encoded_message)

    def test__split_encoded(self):
        response = split_encoded(self.encoded)
        self.assertEqual(response, self.splited_encoded)

    def test__letters_to_indexes(self):
        response = letters_to_indexes(self.four_letters)
        self.assertEqual(response, self.indexes)

    def test__indexes_to_bits(self):
        response = indexes_to_bits(self.indexes)
        self.assertEqual(response, self.bits_decode)

    def test__split_bits(self):
        response = split_bits(self.bits_decode)
        self.assertEqual(response, self.splited_bits_decode)

    def test__translate_splited_bits(self):
        response = translate_splited_bits(self.splited_bits_decode)
        self.assertEqual(response, self.translated_bits_decode)

    def test__b64decode(self):
        response = b64decode(self.encoded_message)
        self.assertEqual(response, self.message)

    def test__all(self):
        self.assertEqual(self.message_for_all, b64decode(b64encode(self.message_for_all)))


if __name__ == '__main__':
    unittest.main()
