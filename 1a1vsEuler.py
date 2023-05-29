import time

def is_prime_traditional(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_prime_euler(n):
    if n <= 1:
        return False

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def totient(n):
        count = 0
        for i in range(1, n+1):
            if gcd(n, i) == 1:
                count += 1
        return count == 2

    return totient(n)

# Número a comprobar
number = 9973

# Comprobación del tiempo utilizando el método tradicional
start_time = time.time()
is_prime = is_prime_traditional(number)
end_time = time.time()

print(f"El número {number} ¿es primo? {is_prime}")
print(f"Tiempo utilizando el método tradicional: {end_time - start_time} segundos")

# Comprobación del tiempo utilizando Totient de Euler
start_time = time.time()
is_prime = is_prime_euler(number)
end_time = time.time()

print(f"El número {number} ¿es primo? {is_prime}")
print(f"Tiempo utilizando Totient de Euler: {end_time - start_time} segundos")
