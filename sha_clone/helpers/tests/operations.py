from sha_clone.helpers.operations import *
import unittest


class TestOperations(unittest.TestCase):
    def setUp(self) -> None:
        self.bits = '11111111000000001111111100000000'
        self.bits_xor_lst = ['11111111111111111111111111111111', '11111111111111111111111111111111',
                             '10101010101010101010101010101010']

        self.bits_add_lst = [
            '01000000000000001111111111111111',
            '01000000000000000000000000000000',
            '01000000000000000000000000000000',
            '01000000000000000000000000000000',
            '01000000000000000000000000000000',

        ]

        self.amount = 16

        self.shifted_right = '00000000000000001111111100000000'

        self.rotated_right = '11111111000000001111111100000000'

        self.xor_ans = '10101010101010101010101010101010'

        self.add_ans = '01000000000000001111111111111111'

    def test__shift_right(self):
        response = shift_right(self.bits, self.amount)
        self.assertEqual(response, self.shifted_right)

    def test__rotate_right(self):
        response = rotate_right(self.bits, self.amount)
        self.assertEqual(response, self.rotated_right)

    def test__xor(self):
        response = xor(self.bits_xor_lst)
        self.assertEqual(response, self.xor_ans)

    def test__add(self):
        response = add(self.bits_add_lst)
        self.assertEqual(response, self.add_ans)


if __name__ == '__main__':
    unittest.main()
