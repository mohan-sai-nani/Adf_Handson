import time
import math


def is_prime(n):
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def next_prime(n):
    prime = n
    found = False
    while not found:
        prime = prime + 1
        if is_prime(prime):
            found = True
    return prime


def print_prime():
    n = 2
    print(n)
    while 1:
        time.sleep(5)
        n = next_prime(n)
        print(n)
        n += 1


if __name__ == '__main__':
    try:
        print_prime()
    except():
        print("An Error Occurred")
