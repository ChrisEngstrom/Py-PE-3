#!/usr/bin/env python3
number = 600851475143

def GetHighestPrimeFactor(number):
    for possiblePrime in reversed(range(2, int_sqrt(number))):
        divisor = number / possiblePrime

        if (divisor.is_integer() and 
            IsPrime(possiblePrime)):
            return possiblePrime

def int_sqrt(n):
    x = n
    y = (x + 1) // 2

    while y < x:
        x = y
        y = (x + n // x) // 2

    return x

def IsPrime(possiblePrimeNumber):
    if (possiblePrimeNumber <= 1):
        return False

    for i in range(2, possiblePrimeNumber):
        if (possiblePrimeNumber % i == 0):
            return False

    return True

print ("The largest prime factor for " + str(number) + " is " + str(GetHighestPrimeFactor(number)))
