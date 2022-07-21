"""
    SHA-256 algorithm based on https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf
"""

from .operations import *

K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]


class SHA256Clone:
    def __init__(self, message):
        self.blocks = []

        if isinstance(message, str):
            self.message = bytearray(message, 'ascii')
        elif isinstance(message, bytes):
            self.message = bytearray(message)
        elif isinstance(message, bytearray):
            self.message = message

        # Set initial hash values
        self.h0 = 0x6a09e667
        self.h1 = 0xbb67ae85
        self.h2 = 0x3c6ef372
        self.h3 = 0xa54ff53a
        self.h5 = 0x9b05688c
        self.h4 = 0x510e527f
        self.h6 = 0x1f83d9ab
        self.h7 = 0x5be0cd19

    def padding(self):
        msg_len = len(self.message) * 8
        self.message.append(0x80)
        while (len(self.message) * 8 + 64) % 512 != 0:
            self.message.append(0x00)

        self.message += msg_len.to_bytes(8, 'big')

        assert (len(self.message) * 8) % 512 == 0, "Padding Error"

    def message_blocks(self):
        for i in range(0, len(self.message), 64):
            self.blocks.append(self.message[i:i + 64])

    def computation(self):
        for message_block in self.blocks:
            message_schedule = []
            for t in range(0, 64):
                if t <= 15:
                    message_schedule.append(bytes(message_block[t * 4:(t * 4) + 4]))

                else:
                    term1 = sigma1(int.from_bytes(message_schedule[t - 2], 'big'))
                    term2 = int.from_bytes(message_schedule[t - 7], 'big')
                    term3 = sigma0(int.from_bytes(message_schedule[t - 15], 'big'))
                    term4 = int.from_bytes(message_schedule[t - 16], 'big')

                    schedule = ((term1 + term2 + term3 + term4) % 2 ** 32).to_bytes(4, 'big')
                    message_schedule.append(schedule)

            assert len(message_schedule) == 64

            a, b, c, d, e, f, g, h = self.h0, self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7

            for t in range(64):
                t1 = ((h + u_sigma1(e) + choice(e, f, g) + K[t] +
                       int.from_bytes(message_schedule[t], 'big')) % 2 ** 32)

                t2 = (u_sigma0(a) + majority(a, b, c)) % 2 ** 32

                h = g
                g = f
                f = e
                e = (d + t1) % 2 ** 32
                d = c
                c = b
                b = a
                a = (t1 + t2) % 2 ** 32

            # Compute intermediate hash value
            self.h0 = (self.h0 + a) % 2 ** 32
            self.h1 = (self.h1 + b) % 2 ** 32
            self.h2 = (self.h2 + c) % 2 ** 32
            self.h3 = (self.h3 + d) % 2 ** 32
            self.h4 = (self.h4 + e) % 2 ** 32
            self.h5 = (self.h5 + f) % 2 ** 32
            self.h6 = (self.h6 + g) % 2 ** 32
            self.h7 = (self.h7 + h) % 2 ** 32

        return (self.h0.to_bytes(4, 'big') + self.h1.to_bytes(4, 'big') +
                self.h2.to_bytes(4, 'big') + self.h3.to_bytes(4, 'big') +
                self.h4.to_bytes(4, 'big') + self.h5.to_bytes(4, 'big') +
                self.h6.to_bytes(4, 'big') + self.h7.to_bytes(4, 'big'))

    def digest(self):
        self.padding()
        self.message_blocks()
        return self.computation()

    def hexdigest(self):
        return self.digest().hex()