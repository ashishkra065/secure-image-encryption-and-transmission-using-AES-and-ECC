from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import HMAC, SHA256
import binascii

class CryptoUtils:
    @staticmethod
    def generate_aes_key(password, salt):
        return scrypt(password, salt, key_len=32, N=2**14, r=8, p=1)

    @staticmethod
    def encrypt_aes(key, data):
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        return cipher.iv + ct_bytes

    @staticmethod
    def decrypt_aes(key, encrypted_data):
        iv = encrypted_data[:AES.block_size]
        ct = encrypted_data[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ct), AES.block_size)

    @staticmethod
    def generate_ecc_key():
        key = ECC.generate(curve='P-256')
        return key

    @staticmethod
    def sign_data(private_key, data):
        hash_obj = SHA256.new(data)
        signer = DSS.new(private_key, 'fips-186-3')
        signature = signer.sign(hash_obj)
        return signature

    @staticmethod
    def verify_signature(public_key, data, signature):
        hash_obj = SHA256.new(data)
        verifier = DSS.new(public_key, 'fips-186-3')
        try:
            verifier.verify(hash_obj, signature)
            return True
        except ValueError:
            return False

    @staticmethod
    def generate_hmac(key, data):
        hmac = HMAC.new(key, digestmod=SHA256)
        hmac.update(data)
        return hmac.digest()
