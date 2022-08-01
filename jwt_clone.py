import json
from hmac import HmacClone
from base64_clone import b64encode, b64decode

SECRET = 'be7ea2ee647b6576d3ee1942410ebcf5'


class JwtClone:
    def __init__(self, token: str = None, header: dict = None, payload: dict = None):
        self.HS256 = HmacClone

        if not token and not (header and payload):
            raise TypeError

        if token:
            self.token = token
            self.header, self.payload, self.signature = token.split('.')
        else:
            self.header = b64encode(json.dumps(header, separators=[',', ':']))
            self.payload = b64encode(json.dumps(payload, separators=[',', ':']))
            self.signature = self.HS256(SECRET, self.header + '.' + self.payload).hexdigest()

            self.signature = b64encode(self.signature)

            self.token = self.header + '.' + self.payload + '.' + self.signature

    def validate(self):
        signature = self.HS256(SECRET, self.header + '.' + self.payload).hexdigest()
        signature = b64encode(signature)

        return self.signature == signature

