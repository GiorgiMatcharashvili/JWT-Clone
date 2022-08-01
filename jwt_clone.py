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


h = {"hi": "hey", "alg": "HS256"}
p = {"sub": "1234567890", "name": "John Doe", "iat": 1516239022}

t = 'eyJoaSI6ImhleSIsImFsZyI6IkhTMjU2In0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.MTZjM2E0YzE3OWU1M2I4NWFlNGYwNmQ3MTkzZjY3YzJkNDI0YWZjODI1NmFkZGY2OTFmYWRhNzVlNWNjMWU1YQ'

j = JwtClone(token=t)
