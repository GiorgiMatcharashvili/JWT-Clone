import json
from hmac import HmacClone
from base64_clone import b64encode, b64decode

SECRET = 'be7ea2ee647b6576d3ee1942410ebcf5'


class JwtClone:
    def __init__(self, token: str = None, header: dict = None, payload: dict = None):
        self._HS256 = HmacClone

        if not token and not (header and payload):
            raise TypeError("__init__() missing required positional argument/s: 'token' or 'header' and 'payload'")

        if token:
            self._token = token
            self._header, self._payload, self._signature = token.split('.')
        else:
            self._header = b64encode(json.dumps(header, separators=[',', ':']))
            self._payload = b64encode(json.dumps(payload, separators=[',', ':']))
            self._signature = self._HS256(SECRET, self._header + '.' + self._payload).hexdigest()

            self._signature = b64encode(self._signature)

            self._token = self._header + '.' + self._payload + '.' + self._signature

        # In case if attacker provides a non-valid signature
        self.authenticate()

        self.validate()

    def validate(self):
        header = b64decode(self._header)
        try:
            header = json.loads(header)
        except:
            try:
                header = json.loads(header[:-1])
            except:
                raise TypeError("header must be a dictionary type")

        if not "typ" in header.keys() or not 'alg' in header.keys():
            raise KeyError("header missing required key/s: 'typ', 'alg'")

        if header['typ'] != "JWT":
            raise TypeError("type of the token must be: 'JWT' ")

        # In case if attacker tries None algorithm method
        # To bypass JSON Web Token controls
        if header['alg'] == 'none' or header['alg'] is None:
            header['alg'] = 'HS256'
            raise TypeError("algorithm of the token can't be a none")

        # In case if attacker tries KID manipulation method to crack the JWT
        if 'kid' in header.keys():
            try:
                int(header['kid'])
            except:
                header['kid'] = '0'
                raise TypeError("value of the 'kid' must be a integer")

    def authenticate(self):
        signature = self._HS256(SECRET, self._header + '.' + self._payload).hexdigest()
        signature = b64encode(signature)

        if self._signature != signature:
            raise Exception('JWT is not valid')
        return True
