from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# AES encryption function
def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return cipher.nonce + tag + ciphertext

# AES decryption function
def aes_decrypt(key, encrypted_data):
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

# Get user input for the key and plaintext
if __name__ == "__main__":
    key_input = input("Enter 16 bytes key in hexadecimal format: ")
    key = bytes.fromhex(key_input)
    
    plaintext = input("Enter plaintext: ").encode()

    encrypted = aes_encrypt(key, plaintext)
    print("Encrypted:", encrypted.hex())

    decrypted = aes_decrypt(key, encrypted)
    print("Decrypted:", decrypted)
#KEY=2b7e151628aed2a6abf7158809cf4f3c