"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME=40
PREPARATION_TIME=2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`."""
    remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining


def preparation_time_in_minutes(number_of_layers):
    """Calculate how many minutes it will take to add the layers.

    :param number_of_layers: int - number of layers.
    :return: int - time in minutes needed to add the layers.

    Function that takes the number of layers you want to add to the lasagna as an
    argument and returns how many minutes you would spend making them, based on
    'PREPARATION_TIME'."""
    time = PREPARATION_TIME * number_of_layers
    return time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return elapsed cooking time.

    :param number_of_layers: int - number of layers.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - elapsed time (in minutes).

    This function should return the total number of minutes you've been cooking,
    or the sum of your preparation time and the time the lasagna has already
    spent baking in the oven."""
    elapsed_time = elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
    return elapsed_time
