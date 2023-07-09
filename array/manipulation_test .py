import numpy as np


def test_reshape():
    # Create a 1D NumPy array
    my_array = np.array([1, 2, 3, 4, 5, 6])
    # Reshape the array into a 2D array with 2 rows and 3 columns
    reshaped_array = np.reshape(my_array, (2, 3))
    assert reshaped_array.shape == (2, 3)

    # Create a 1D NumPy array
    my_array = np.array([1, 2, 3, 4, 5, 6])
    # Reshape the array into a 2D array with 3 rows and an automatically calculated number of columns
    reshaped_array = np.reshape(my_array, (3, -1))
    assert reshaped_array.shape == (3, 2)

def test_concatenate():
    # Create two NumPy arrays
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])

    # Concatenate the arrays along the default axis (axis=0)
    concatenated_array = np.concatenate((array1, array2))    
    assert np.array_equal(concatenated_array, np.array([1, 2, 3, 4, 5, 6]))


def test_sort():   
    # Create a NumPy array
    my_array = np.array([4, 2, 5, 1, 3])
    # Sort the array
    sorted_array = np.sort(my_array)
    assert np.array_equal(sorted_array, np.array([1, 2, 3, 4, 5]))