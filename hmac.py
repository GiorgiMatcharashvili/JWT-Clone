"""
    HMAC algorithm based on https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.198-1.pdf
"""

from sha256_clone import SHA256Clone


class HmacClone:
    def __init__(self, key, text):
        self.inner_pads = bytearray()
        self.outer_pads = bytearray()

        if isinstance(text, str):
            self.message = bytearray(text, 'ascii')
        elif isinstance(text, bytes):
            self.message = bytearray(text)

        if isinstance(key, str):
            self.key = bytearray(key, 'ascii')
        elif isinstance(key, bytes):
            self.key = bytearray(key)

        self.block_size = 64

        # Approved Hash Function
        self.AHF = SHA256Clone

    def preprocessing_key(self):
        if len(self.key) > self.block_size:
            self.key = bytearray(self.AHF(self.key).digest())
        elif len(self.key) < self.block_size:
            self.key += b"\x00" * (self.block_size - len(self.key))

    def init_pads(self):
        for i in range(self.block_size):
            self.inner_pads.append(0x36 ^ self.key[i])
            self.outer_pads.append(0x5c ^ self.key[i])

    def digest(self):
        self.preprocessing_key()
        self.init_pads()

        append_inner = bytes(self.inner_pads) + self.message
        hashed_inner = self.AHF(append_inner).digest()

        append_outer = self.outer_pads + hashed_inner

        return self.AHF(append_outer).digest()

    def hexdigest(self):
        return self.digest().hex()

m = 'hhkwehrkhwrhuiewfhihwiuehfewuoifiuwebfiebfiuh9pgr72378t562t5y0892u9 23'

k = '213618726478916c16c4'

h = HmacClone(k, m)

print(h.hexdigest())
