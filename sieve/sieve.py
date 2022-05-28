"""Use the Sieve of Eratosthenes to find all the primes
from 2 up to a given number."""

def primes(limit):
    """Use the Sieve of Eratosthenes to find all the primes
    from 2 up to a given number.

    :param limit: int - the number that limit the search
    """

    available = set(range(2,limit+1))   # Generate list from 2 to limit
    prime = 1    # First prime number
    primes_list = [] # To store list of found primes

    while len(available) != 0:
        prime += 1   # guest next prime value
        while prime not in available : # Check if guessed prime is in the list
            prime += 1  # if not, guess again

        primes_list.append(prime)

        # Remove from available all multiples of the prime
        for number in range(prime, limit+1, prime):
            if number in available:
                available.remove(number)

    return primes_list
