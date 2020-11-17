from cryptography.hazmat.backends import default_backend as backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096, backend=backend())
#public_key = private_key.public_key
public_key = private_key.public_key()

message = b"More secrets go here"

encrypted = public_key(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),
                                             label=None))
print(encrypted)

decrypted = private_key.decrypt(encrypted, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                        algorithm=hashes.SHA256(), label=None))

print(decrypted)
