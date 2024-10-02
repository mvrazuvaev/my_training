numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
k = 0
for i in numbers[1:]:
    for j in range(2, i):
        if i % j == 0:
            k = k+1
    if k == 0:
        is_prime = True
        primes.append(i)
    else:
        is_prime = False
        not_primes.append(i)
        k = 0
print('Primes:', primes)
print('Not Primes:', not_primes)
