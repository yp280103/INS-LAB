def encrypt(plain_text, key):
    encrypted_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = key[i]
        encrypted_char = chr((ord(char) + ord(key_char)) % 128)
        encrypted_text += encrypted_char
    return encrypted_text


def decrypt(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        key_char = key[i]
        decrypted_char = chr((ord(char) - ord(key_char)) % 128)
        decrypted_text += decrypted_char
    return decrypted_text


# User input
plain_text = input("Enter the plain text: ")  
key = input("Enter the key (same length as plain text): ")

# Encryption
encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

# Decryption
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)