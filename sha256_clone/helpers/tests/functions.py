from sha256_clone.helpers.functions import *
import unittest


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.sigma_bits = '00000000000000000011111111111111'
        self.bits_lst = [
            '00000000111111110000000011111111',
            '00000000000000001111111111111111',
            '11111111111111110000000000000000'
        ]

        self.sigma0_ans = '11110001111111111100011110000000'

        self.sigma1_ans = '00011000000000000110000000001111'

        self.u_sigma0_ans = '00111111000001111111001111111110'

        self.u_sigma1_ans = '00000011111111111111111101111000'

        self.choice_ans = '11111111000000000000000011111111'

        self.majority_ans = '00000000111111110000000011111111'

    def test__sigma0(self):
        response = sigma0(self.sigma_bits)
        self.assertEqual(response, self.sigma0_ans)

    def test__sigma1(self):
        response = sigma1(self.sigma_bits)
        self.assertEqual(response, self.sigma1_ans)

    def test__u_sigma0(self):
        response = u_sigma0(self.sigma_bits)
        self.assertEqual(response, self.u_sigma0_ans)

    def test__u_sigma1(self):
        response = u_sigma1(self.sigma_bits)
        self.assertEqual(response, self.u_sigma1_ans)

    def test__choice(self):
        response = choice(self.bits_lst)
        self.assertEqual(response, self.choice_ans)

    def test__majority(self):
        response = majority(self.bits_lst)
        self.assertEqual(response, self.majority_ans)


if __name__ == '__main__':
    unittest.main()
