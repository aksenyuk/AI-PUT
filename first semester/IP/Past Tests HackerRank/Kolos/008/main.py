def isPrime(s):
    return not(bool([True for i in range(2, int(s)//2) if int(s) % i == 0]))
print(isPrime(6))