numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
primes = []
not_primes = []
for i in numbers:
    num = numbers[i - 1]
    if num > 1:
        for j in range(2, (num // 2) + 1 ):
            if (num % j) == 0:
                not_primes.append(num)
                break
        else:
            primes.append(num)
    #else:
    #    not_primes.append(num)
print(primes)
print(not_primes)