import random

import sympy


def generate_good_prime(prime_min, prime_max): #good meaning 4 mod 3
    return sympy.randprime(prime_min, prime_max)

def find_prime_factors(x):
    prime_factors = []
    for i in range(2, x):
        if x % i == 0 and sympy.isprime(i):
            prime_factors.append(i)
    return prime_factors



def find_prime_root(n):
    euler = n-1
    prime_factors = find_prime_factors(euler)
    d =[]
    for i in range(1,n):
        if n%i == 0:
            d.append(i)
    for i in range(2, len(prime_factors)):
        g = random.choice(prime_factors)
        for power in d:
            if (pow(g, power))%(n-1) ==1:
                break
        return g
    return -1


def a_or_b_create_x_or_y(n, g, y_min=100, y_max=1000):
    power = random.randint(y_min, y_max)
    y = pow(g, power)%n
    return y, power

def calculate_k(n, x_or_y, power):
    k = pow(x_or_y, power)%n
    return k

def task():
    g = -1
    n = -1
    while g == -1:
        n_pretender = generate_good_prime(1000, 9999)
        g = find_prime_root(n_pretender)
        if g == -1:
            continue
        n = n_pretender
    #A task
    x_from_a, power_from_a = a_or_b_create_x_or_y(n, g)

    #B task
    y_from_b, power_from_b = a_or_b_create_x_or_y(n, g)

    #Now A sends B the X and B sends A the Y
    #what A does:
    k_a = calculate_k(n, y_from_b, power_from_a)

    #what B does:
    k_b = calculate_k(n, x_from_a, power_from_b)

    if k_a == k_b:
        print("A and B have the same key")

task()