"""Determine if a number is perfect, abundant, or deficient
based on Nicomachus' (60 - 120 CE) classification scheme
for positive integers."""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = []
    for guessed_factor in range(1, int(number/2)+1):
        if number % guessed_factor == 0:
            factors.append(guessed_factor)

    aliquot_sum = sum(factors)
    response = ''

    if aliquot_sum == number:
        response = 'perfect'
    else:
        response = 'abundant' if aliquot_sum > number else 'deficient'

    return response
