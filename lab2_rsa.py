import sympy
import random
import math


def generate_good_prime(prime_min, prime_max): #good meaning 4 mod 3
    return sympy.randprime(prime_min, prime_max)

def generate_e(num, min = 3, max = 2**8):
    while True:
        x = random.randint(min, max)
        if math.gcd(x, num) == 1:
            return x
def generate_d(e, phi, max = 2**8):
    d = random.randint(1, max)
    while e * d % phi != 1:
        d+= 1
    return d


def cypher(e, n, message):
    return [pow(int(digit), e, n) for digit in message]

def decipher(d, n, cyphered):
    return [pow(int(num), d, n) for num in cyphered]


def create_random_message(length):
    message = []
    for i in range(length):
        message.append(random.randint(0, 9))
    return message

def calculate_keys(prime_min, prime_max):
    p = generate_good_prime(prime_min, prime_max)
    q = generate_good_prime(prime_min, prime_max)
    while p == q:
        q = generate_good_prime(prime_min, prime_max)
    n = p * q
    phi = (p-1)*(q-1)
    e = generate_e(phi, 2, n)
    d = generate_d(e, phi, n)

    return n, e, d
def check_if_same(message, deciphered):
    for i in range(len(message)):
        if message[i] != deciphered[i]:
            return False
    return True

def task():
    n, e, d = calculate_keys(1000, 9999)
    message = create_random_message(50)
    print("Message: ", message)
    cyphered = cypher(e, n, message)
    print("Cyphered: ", cyphered)
    deciphered = decipher(d, n, cyphered)
    print("Deciphered: ", deciphered)
    print("Same: ", check_if_same(message, deciphered))

task()