import math
import random
import sympy


def generate_good_prime(bit_length): #good meaning 4 mod 3
    while True:
        prime = sympy.randprime(2**(bit_length-1), 2**bit_length)
        if prime % 4 == 3:
            return prime

def generate_coprime_x(n):
    while True:
        x = random.randint(2, n-1)
        if math.gcd(x, n) == 1:
            return x

def generator(x, n, number):
    values = []
    value = (x**2)%n
    values.append(value%2)
    for i in range(1, number):
        value = (value**2)%n
        values.append(value%2)

    return values

def test1(values):
    test_sum = sum(values)
    if 9725 < test_sum < 10275:
        return True
    else:
        return False

def test2(values):
    series = 1
    series_type = values[0]
    ranges_0 = [0]*7
    ranges_1 = [0]*7
    for i in range(1, 20000):
        if values[i] == series_type:
            series += 1
        else:
            if series >= 6:
                if series_type == 0:
                    ranges_0[6] += 1
                else:
                    ranges_1[6] += 1
            else:
                if series_type == 0:
                    ranges_0[series] += 1
                else:
                    ranges_1[series] += 1

            series_type = values[i]
            series = 1

    if 2315<ranges_1[1]<2685 and 1114<ranges_1[2]<1386 and 527<ranges_1[3]<723 and 240<ranges_1[4]<384 and 103<ranges_1[5]<209 and 103<ranges_1[6]<209:
        if 2315<ranges_0[1]<2685 and 1114<ranges_0[2]<1386 and 527<ranges_0[3]<723 and 240<ranges_0[4]<384 and 103<ranges_0[5]<209 and 103<ranges_0[6]<209:
            return True
        else:
            return False
    else:
        return False

def test3(values):
    length = 0
    type = -1
    for i in range(20000):
        if type == values[i]:
            length += 1
        else:
            if length > 26:
                return False
            length = 1
            type = values[i]

    return True

def test4(values):
    blocks = [0]*16
    for i in range(0, 20000 - 3, 4):
        block = values[i:i + 4]
        block_str = ''.join(map(str, block))
        num = int(block_str, 2)
        blocks[num] +=1
    summing = 0
    for i in range(16):
        summing += blocks[i]**2
    x = 16/5000*summing-5000

    if 2.16 < x < 46.17:
        return True
    else:
        return False


def ___main___(length, key_bits):
    p = generate_good_prime(key_bits)
    q = generate_good_prime(key_bits)
    while p == q:
        q = generate_good_prime(key_bits)
    print("p: ", p)
    print("q: ", q)
    n = p * q
    x = generate_coprime_x(n)
    generated = generator(x, n, length)
    print(generated)

    print("Tests? (configured for 20000 bits): (0/1)")
    tests = int(input())
    if tests == 1:
        print("Test pojedynczych bitów :" + str(test1(generated)))
        print("Test serii :" + str(test2(generated)))
        print("Test długiej serii :" + str(test3(generated)))
        print("Test pokerowy :" + str(test4(generated)))




print("Enter the length of the sequence: ")
length = input()
print("Enter the number of bits in the key: ")
key_bits = input()
___main___(int(length), int(key_bits))
