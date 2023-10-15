import string
def generate_key():
    key = {}
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        substitution = input("Enter substitution for {}: ".format(letter))
        key[letter] = substitution.lower()
    return key

def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.lower():
        if char.isalpha():
            ciphertext += key[char]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext.lower():
        if char.isalpha():
            for k, v in key.items():
                if v == char:
                    plaintext += k
                    break
        else:
            plaintext += char
    return plaintext

def main():
    key = generate_key()

    plaintext = input("Enter plaintext: ")
    encrypted_text = encrypt(plaintext, key)
    decrypted_text = decrypt(encrypted_text, key)

    print("Plaintext: ", plaintext)
    print("Encrypted text: ", encrypted_text)
    print("Decrypted text: ", decrypted_text)

if __name__ == "__main__":
    main()
