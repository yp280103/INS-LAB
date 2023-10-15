def create_monoalphabetic_key(alphabet, shuffled_alphabet):
    return {alphabet[i]: shuffled_alphabet[i] for i in range(26)}

def monoalphabetic_encrypt(text, key):
    return ''.join(key.get(char, char) for char in text)

def monoalphabetic_decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    return ''.join(reverse_key.get(char, char) for char in ciphertext)

# Example usage:
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shuffled_alphabet = 'zxcvbnmasdfghjklqwertyuiop'
key = create_monoalphabetic_key(alphabet, shuffled_alphabet)

plaintext = "hello world"
encrypted = monoalphabetic_encrypt(plaintext, key)
decrypted = monoalphabetic_decrypt(encrypted, key)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
