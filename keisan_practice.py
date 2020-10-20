import random
import copy


def trial_division(n):
    """Return a list of the prime factors for a natural number."""
    if n < 2:
        return []
    prime_factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            prime_factors.append(i)
            n //= i

    if n > 1:
        prime_factors.append(n)

    return prime_factors


def keisan(method):
    if method == '+':
        a = random.randint(1, 99)
        b = random.randint(1, 100 - a)
        return a, b
    elif method == '-':
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        return max([a, b]), min([a, b])
    elif method == '*':
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        return a, b
    elif method == '%':
        a = random.randint(1, 99)
        primes = trial_division(a)
        if len(primes) == 0:
            b = 1
        else:
            num = random.randint(1, len(primes))
            prime_nums = random.sample(primes, num)
            b = 1
            for i in prime_nums:
                b *= i
        return a, b


def main():
    for _ in range(20):
        temp = copy.deepcopy(calc_temp)
        method = random.choice(method_of_calc)
        a, b = keisan(method)
        temp[0] = str(a)
        temp[1] = method
        temp[2] = str(b)
        drill.append(temp)

    for formula in drill:
        print(' '.join(formula))


if __name__ == '__main__':
    drill = []
    calc_temp = ['a', '+', 'b', '=']
    method_of_calc = ('+', '-', '*', '%')
    main()

