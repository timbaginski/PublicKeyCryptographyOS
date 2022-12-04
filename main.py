def read_primes():
    f = open("primes.txt", "r")
    primes = f.read().split(", ")
    print(primes)
    return primes

read_primes()
    






