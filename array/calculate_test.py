import numpy as np


def test_mean():
    # Create a NumPy array
    my_array = np.array([1, 2, 3, 4, 5])
    # Calculate the mean of the array
    mean_value = np.mean(my_array)
    assert mean_value == 3.0


def test_sum():
    # Create a NumPy array
    my_array = np.array([1, 2, 3, 4, 5])

    # Calculate the sum of the array
    sum_value = np.sum(my_array)
    assert sum_value == 15


def test_max():
    # Create a NumPy array
    my_array = np.array([1, 2, 3, 4, 5])

    # Calculate the maximum value of the array
    max_value = np.max(my_array)
    assert max_value == 5


def test_min():
    # Create a NumPy array
    my_array = np.array([1, 2, 3, 4, 5])

    # Calculate the minimum value of the array
    min_value = np.min(my_array)
    assert min_value == 1


def test_argmax():
    # Create a NumPy array
    my_array = np.array([1, 2, 3, 4, 5])

    # Calculate the index of the maximum value of the array
    argmax_value = np.argmax(my_array)
    assert argmax_value == 4

def test_argmin():
    # Create a NumPy array
    my_array = np.array([1, 2, 3, 4, 5])

    # Calculate the index of the minimum value of the array
    argmin_value = np.argmin(my_array)
    assert argmin_value == 0

def test_dot():
    # Create two NumPy arrays
    my_array_1 = np.array([1, 2, 3, 4, 5])
    my_array_2 = np.array([6, 7, 8, 9, 10])

    # Calculate the dot product of the two arrays
    dot_value = np.dot(my_array_1, my_array_2)
    assert dot_value == 130    