import random


def miller_rabin(n, tries):
    k = 0
    q = 0
    if n == 1 or n == 2 or n == 3:
        print(f'N = {n} is a prime.')
        return

    Stop = True
    factor = n - 1
    while (Stop):  # --> find prime factorization for n-1 = 2^k x q
        if factor % 2 == 0:
            factor = int(factor / 2)
            k += 1
        else:
            q = int(factor)
            Stop = False

    if n % 2 == 0:
        print(f'N = {n} is even, so it is a composite number.')
        return

    notWitness = []  # --> List of not witnesses a if N was not a composite.
    for _ in range(1, tries + 1):
        a = int(random.randrange(2, n - 1))
        x = pow(a, int(q), int(n))

        notWitness.append(a)
        if x != 1:  # Cond 1
            for i in range(k):  # Cond 2 from [ i=0 to i=k-1]
                x = pow(a, pow(2, i) * int(q), n)
                if x != n - 1:
                    if i == k - 1:
                        print(f'--> N = {n} is composite and a= {a} is a witness.')
                        return
                else:
                    break

    print(f'--> N = {n} is more probably is prime, after we tried with a = {notWitness}.')


if __name__ == '__main__':
    N = int(input("Enter a Number: "))
    numberOfTries = int(input("How many time do you want to repeat the test ?  "))
    miller_rabin(N, numberOfTries)
