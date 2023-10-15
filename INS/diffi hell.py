import random

p = 23  # Prime number
g = 5   # Primitive root of p

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

private_key_candidate1 = random.randint(2, p - 2)

public_key_candidate1 = mod_exp(g, private_key_candidate1, p)

private_key_candidate2 = random.randint(2, p - 2)

public_key_candidate2 = mod_exp(g, private_key_candidate2, p)

# Key exchange phase
# Shared secret calculation for Candidate 1
shared_secret_candidate1 = mod_exp(public_key_candidate2, private_key_candidate1, p)

# Shared secret calculation for Candidate 2
shared_secret_candidate2 = mod_exp(public_key_candidate1, private_key_candidate2, p)

# Both candidates should now have the same shared secret
print("Candidate 1's public key:", public_key_candidate1)
print("Candidate 1's private key:", private_key_candidate1)
print("Candidate 2's public key:", public_key_candidate2)
print("Candidate 2's private key:", private_key_candidate2)
print("Shared secret for Candidate 1:", shared_secret_candidate1)
print("Shared secret for Candidate 2:", shared_secret_candidate2)
