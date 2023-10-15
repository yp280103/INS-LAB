# Function to encrypt a message using a 3x3 matrix transposition
def encrypt(message):
    if len(message) != 9:
        print("error")

    encrypted_message = [
        message[0] + message[3] + message[6],
        message[1] + message[4] + message[7],
        message[2] + message[5] + message[8]
    ]

    return ''.join(encrypted_message)

# Function to decrypt a message using a 3x3 matrix transposition
def decrypt(encrypted_message):
    if len(encrypted_message) != 9:
        raise ValueError("Encrypted message length must be exactly 9 characters.")

    decrypted_message = [
        encrypted_message[0] + encrypted_message[3] + encrypted_message[6],
        encrypted_message[1] + encrypted_message[4] + encrypted_message[7],
        encrypted_message[2] + encrypted_message[5] + encrypted_message[8]
    ]

    return ''.join(decrypted_message)

# Input
message = input("Enter the 9-character message to encrypt: ")

# Encrypt the message
encrypted_message = encrypt(message)
print("Encrypted Message:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)
