import hashlib
import random
import string
import time
import matplotlib.pyplot as plt
import numpy as np

def create_random_message(length):
    message = []
    characters = string.ascii_letters + string.digits
    for i in range(length):
        message.append(random.choice(characters))
    return message


def save_to_file(string, file_name):
    f = open(file_name, 'w')
    f.write(string)
    f.close()

def prepare_5_samples(length1, length2, length3, length4):
    m1 = create_random_message(length1)
    m2 = create_random_message(length2)
    m3 = create_random_message(length3)
    m4 = create_random_message(length4)

    save_to_file(''.join(m1), 'sample1.txt')
    save_to_file(''.join(m2), 'sample2.txt')
    save_to_file(''.join(m3), 'sample3.txt')
    save_to_file(''.join(m4), 'sample4.txt')

def read_from_file(file_name):
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content

def algorithms_and_time(string,for_ploting):
    length = len(string)
    algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']
    for a in algorithms:
        start = time.time()
        hasher = hashlib.new(a, string.encode())
        hash = hasher.hexdigest()
        end = time.time()
        time_elapsed =  end - start
        print(f'{a}: time = {time_elapsed:.10f} seconds, output length: {len(hash)}, output: {hash}')
        for_ploting[a][length] = time_elapsed
    print("\n")
    return for_ploting

def task1and2():
    for_ploting = {algo: {} for algo in ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
                                         'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']}
    print("for sample1.txt:")
    for_ploting = algorithms_and_time(read_from_file('sample1.txt'), for_ploting)
    print("for sample2.txt:")
    for_ploting = algorithms_and_time(read_from_file('sample2.txt'), for_ploting)
    print("for sample3.txt:")
    for_ploting = algorithms_and_time(read_from_file('sample3.txt'), for_ploting)
    print("for sample4.txt:")
    for_ploting = algorithms_and_time(read_from_file('sample4.txt'), for_ploting)
    return for_ploting

def task3():
    word = "koza"
    print("for word koza:")
    print(hashlib.md5(word.encode()).hexdigest())


def task5(length):
    collisions = 0
    hashes = {}
    for i in range(100000):
        message = create_random_message(100)
        message_string = ''.join(message)
        hash = hashlib.sha3_384(message_string.encode()).hexdigest()
        hash_bits = bin(int(hash, 16))[2:].zfill(384)[:length]

        if hash_bits in hashes:
            collisions += 1
        else:
            hashes[hash_bits] = message_string
    print("Collisions: ", collisions)


def task6():
    characters = 100
    message = create_random_message(characters)
    string_message = ''.join(message)
    hash1 = hashlib.sha3_224(string_message.encode()).hexdigest()

    message_bytes = bytearray(string_message, 'utf-8')
    byte_index = random.randint(0, len(message_bytes)-1)
    bit_index = random.randint(0, 7)

    message_bytes[byte_index] ^= (1 << bit_index)

    modified_message = message_bytes.decode('utf-8')

    hash2 = hashlib.sha3_224(modified_message.encode()).hexdigest()

    bin_hash1 = bin(int(hash1, 16))[2:].zfill(224)
    bin_hash2 = bin(int(hash2, 16))[2:].zfill(224)
    changed_bits = sum(1 for a, b in zip(bin_hash1, bin_hash2) if a != b)

    percent = (changed_bits / 224) * 100
    print(f"Percentage of changed bits: {percent:.2f}%")
    if 48 <= percent <= 52:
        print("SAC conditions are met")
    else:
        print("SAC conditions are not met")

def task2_print_plot(for_ploting):
    algorithms = list(for_ploting.keys())
    sample_sizes = sorted(next(iter(for_ploting.values())).keys())
    num_algorithms = len(algorithms)
    num_samples = len(sample_sizes)

    bar_width = 0.15
    x = np.arange(num_algorithms)

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, sample_size in enumerate(sample_sizes):
        values = [for_ploting[algo][sample_size] for algo in algorithms]
        ax.bar(x + i * bar_width, values, width=bar_width, label=f"{sample_size}")

    ax.set_xlabel('Algorytmy')
    ax.set_ylabel('Czas (sekundy)')
    ax.set_title('Czas wykonania algorytmów hashujących')
    ax.set_xticks(x + (num_samples / 2 - 0.5) * bar_width)
    ax.set_xticklabels(algorithms, rotation=45)
    ax.legend(title="Długość tekstu")

    plt.tight_layout()
    plt.show()


def run_all_tasks():
    print("ZAD1 i ZAD2")
    for_ploting = task1and2()
    task2_print_plot(for_ploting)
    print("ZAD3")
    task3()
    print("ZAD5")
    task5(12)
    print("ZAD6")
    task6()

#preparing samples(done before run_all_tasks, but it can be omited if done in previous run)
#prepare_5_samples(10000, 100000, 500000, 1000000)

run_all_tasks()