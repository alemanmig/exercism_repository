"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
print(EXPECTED_BAKE_TIME)

PREPARATION_TIME = 2

def bake_time_remaining(elaps_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elaps_bake_time
    
bake_time_remaining(30)

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation_time_in_minutes()
    Parameters:
        numbers_of_layers(int): The number of layers you want in the lasagna
    Returns:
        int: minutes you would spend making them
    Function that takes the number_of_layers you want to add to the lasagna as an argument
    and returns how    many minutes you would spend making them. Assume each layer takes 2 minutes
    to prepare."""
    return number_of_layers * PREPARATION_TIME

preparation_time_in_minutes(2)


def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the elapsed_time_in_minutes()
    Parameters:
        number_of_layers(int):the number of layers added to the lasagna
        elapsed_bake_time(int): number of minutes the lasagna has spent baking in the oven already
    Returns: 
        elapsed_time_in_minutes the lasagna have been in the kitchen cooking 
    Function that should return the total minutes you have been in the kitchen cooking
    — your preparation time layering + the time the lasagna has spent baking in the oven.
    """
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time

print("Elapse time", elapsed_time_in_minutes(3,20))


