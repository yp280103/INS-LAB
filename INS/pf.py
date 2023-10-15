def generate_playfair_matrix(key):
    key = key.replace('J', 'I')
    key = key.upper()
    key = key.replace(' ', '')
    key += 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    matrix = [['' for _ in range(5)] for _ in range(5)]
    chars_added = set()

    i, j = 0, 0
    for char in key:
        if char not in chars_added:
            matrix[i][j] = char
            chars_added.add(char)
            j += 1
            if j == 5:
                i += 1
                j = 0

    return matrix

def get_char_positions(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt(message, key):
    matrix = generate_playfair_matrix(key)
    message = message.replace('J', 'I')
    message = message.upper()
    message = message.replace(' ', '')

    i = 0
    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message = message[:i + 1] + 'X' + message[i + 1:]
        i += 2

    if len(message) % 2 != 0:
        message += 'X'

    ciphertext = ''
    i = 0
    while i < len(message):
        char1 = message[i]
        char2 = message[i + 1]

        row1, col1 = get_char_positions(matrix, char1)
        row2, col2 = get_char_positions(matrix, char2)

        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            temp = col1
            col1 = col2
            col2 = temp

        ciphertext += matrix[row1][col1]
        ciphertext += matrix[row2][col2]

        i += 2

    return ciphertext

def decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace(' ', '')  # Removing spaces

    plaintext = ''
    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = get_char_positions(matrix, char1)
        row2, col2 = get_char_positions(matrix, char2)

        if row1 == row2:
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            temp = col1
            col1 = col2
            col2 = temp

        plaintext += matrix[row1][col1]


def main():
    key = input("Enter the encryption key: ")
    message = input("Enter the message to encrypt: ")

    ciphertext = encrypt(message, key)

    print("Encrypted message:", ciphertext)

if __name__ == "__main__":
    main()