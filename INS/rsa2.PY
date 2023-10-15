import math

p_prime = int(input("first prime number: "))
q_prime = int(input("second prime number: "))
n = p_prime * q_prime
print("n =", n)
phi = (p_prime - 1) * (q_prime - 1)
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1
print("e =", e)
k = 2
d = ((k * phi) + 1) / e
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
msg = 54
print(f'Original message: {msg}')
C = pow(msg, e, n)
print(f'Encrypted message: {C}')
M = pow(C, int(d), n)
print(f'Decrypted message: {M}')

