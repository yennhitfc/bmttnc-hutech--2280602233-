import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256



class RSACipher:
    def __init__(self):
        self.private_key_path = "private.pem"
        self.public_key_path = "public.pem"

    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open(self.private_key_path, "wb") as f:
            f.write(private_key)
        with open(self.public_key_path, "wb") as f:
            f.write(public_key)

    def load_keys(self):
        with open(self.private_key_path, "rb") as f:
            private_key = RSA.import_key(f.read())
        with open(self.public_key_path, "rb") as f:
            public_key = RSA.import_key(f.read())
        return private_key, public_key

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.encrypt(message.encode())

    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(ciphertext).decode()

    def sign(self, message, private_key):
        h = SHA256.new(message.encode())
        signature = pkcs1_15.new(private_key).sign(h)
        return signature

    def verify(self, message, signature, public_key):
        h = SHA256.new(message.encode())
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False
