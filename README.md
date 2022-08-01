# JWT-Clone
My goal was to implement base64, SHA-256 and HMAC algorithms from scratch using only pure python and create JWT logic using these algorithms.

# Description
JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.

Although JWTs can be encrypted to also provide secrecy between parties, we will focus on signed tokens. Signed tokens can verify the integrity of the claims contained within it, while encrypted tokens hide those claims from other parties. When tokens are signed using public/private key pairs, the signature also certifies that only the party holding the private key is the one that signed it.

# Getting started
If you want to test or use my implementation import or open a file named jwt_clone.py, create an object from class JwtClone, you can send it a token or header and payload. Use validate method to check a token.
 
# How does it works
To implement JWT logic, you need three things simple encryption/decryption algorithm(I am using standard base64), a hash algorithm(SHA-256), and an HMAC algorithm.
 
# Credits
@inc. all by myself
