numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for n in numbers:
    is_prime = True
    if n == 1:
        continue
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)
print('Primes: ', primes)
print('Not_primes: ', not_primes)

"""
Вывод на консоль:
Primes: [2, 3, 5, 7, 11, 13]
Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
"""