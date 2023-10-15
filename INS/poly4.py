def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            char = char.upper()
            char_index = ord(char) - ord('A')
            key_char = key[key_index % len(key)].upper()
            key_index += 1
            key_index %= len(key)

            key_shift = ord(key_char) - ord('A')
            encrypted_index = (char_index + key_shift) % 26
            encrypted_char = chr(encrypted_index + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            char = char.upper()
            char_index = ord(char) - ord('A')
            key_char = key[key_index % len(key)].upper()
            key_index += 1
            key_index %= len(key)

            key_shift = ord(key_char) - ord('A')
            decrypted_index = (char_index - key_shift) % 26
            decrypted_char = chr(decrypted_index + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Example usage:
plaintext = input("Enter Text to encrpt-")
key = input("Enter Key-")

encrypted = encrypt(plaintext, key)
decrypted = decrypt(encrypted, key)


print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
