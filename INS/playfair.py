def print_matrix(m):
    print("\nMatrix:")
    for i in m:
        print(i)


def not_in_matrix(key, m):
    for i in m:
        for j in i:
            if key == j:
                return False
    return True


def get_index(key, m):
    for i, k1 in enumerate(m):
        for j, k2 in enumerate(k1):
            if key == k2:
                return [i, j]
    return [-1, -1]


key = "monarchy"
text = "instrument"

print("\nText:", text)
print("Key:", key)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

matrix = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]


i = j = k = 0

while k < len(key):
    if not_in_matrix(key[k], matrix):
        if j == 5:
            i += 1
            j = 0
        matrix[i][j] = key[k]
        j += 1
    k += 1

for a in alpha:
    if not_in_matrix(a, matrix):
        if j == 5:
            i += 1
            j = 0
        matrix[i][j] = a
        j += 1

print_matrix(matrix)

split = []
i = 0

while i < len(text):
    s = text[i:i+2]

    if len(s) == 1:
        s += "z"

    if s[0] == s[1]:
        split.append(s[0]+"x")
        i += 1
    else:
        split.append(s)
        i += 2

encoded = []
for i in split:
    v1 = i[0]
    v2 = i[1]

    i1 = get_index(v1, matrix)
    i2 = get_index(v2, matrix)

    v1_i = i1[0]
    v1_j = i1[1]
    v2_i = i2[0]
    v2_j = i2[1]

    if v1_i == v2_i:
        encoded.append(matrix[v1_i][(v1_j+1) % 5] + matrix[v2_i][(v2_j+1) % 5])

    elif v1_j == v2_j:
        encoded.append(matrix[(v1_i+1) % 5][v1_j] + matrix[(v2_i+1) % 5][v2_j])

    else:
        encoded.append(matrix[v1_i][v2_j] + matrix[v2_i][v1_j])

encoded = "".join(encoded)
print("Encoded: ", encoded)
split = []
i = 0

while i < len(encoded):
    s = encoded[i:i+2]

    split.append(s)
    i += 2

decoded = []

for i in split:
    v1 = i[0]
    v2 = i[1]

    i1 = get_index(v1, matrix)
    i2 = get_index(v2, matrix)

    v1_i = i1[0]
    v1_j = i1[1]
    v2_i = i2[0]
    v2_j = i2[1]

    if v1_i == v2_i:
        decoded.append(matrix[v1_i][(v1_j-1) % 5] + matrix[v2_i][(v2_j-1) % 5])

    elif v1_j == v2_j:
        decoded.append(matrix[(v1_i-1) % 5][v1_j] + matrix[(v2_i-1) % 5][v2_j])

    else:
        decoded.append((matrix[v2_i][v1_j] + matrix[v1_i][v2_j])[::-1])

decoded = "".join(decoded)
print("\nDecoded:", decoded)