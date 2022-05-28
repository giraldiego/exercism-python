"""Sum Of Multiples exercise"""

def sum_of_multiples(limit, multiples):
    """Given a number, find the sum of all the unique multiples of particular
    numbers up to but not including that number.

    :param limit: int -
    :param multiples: list of int -
    Assumptions:
    - All input numbers are non-negative ints, i.e. natural numbers including zero.
    - A list of factors must be given, and its elements are unique and sorted
    in ascending order.
    """
    result = set()
    non_zero_multiples = [x for x in multiples if x != 0]

    for factor in non_zero_multiples:
        for num in range(factor, limit, factor):
            result.add(num)

    return sum(result)
