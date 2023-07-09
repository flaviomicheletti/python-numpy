import numpy as np


def test_create_array():
    # Create an array from 0 to 4 with a default step of 1
    my_array = np.arange(5)
    expected_array = np.array([0, 1, 2, 3, 4])
    assert np.array_equal(my_array, expected_array)

    #  Create an array from 0 to 10 with a step of 2
    my_array = np.arange(0, 10, 2)
    expected_array = np.array([0, 2, 4, 6, 8])
    assert np.array_equal(my_array, expected_array)

    # Create a reversed array from 10 to 1 with a step of -1
    my_array = np.arange(10, 0, -1)
    expected_array = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert np.array_equal(my_array, expected_array)

    # Create an array from 0 to 2.5 with a step of 0.5
    my_array = np.arange(0, 2.5, 0.5)
    expected_array = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
    assert np.array_equal(my_array, expected_array)


def test_zeros():
    # Create a NumPy_zeros filled with zeros
    my_array = np.zeros(5)
    expected_array = np.array([0, 0, 0, 0, 0])
    assert np.array_equal(my_array, expected_array)

    # Create a 2D NumPy array (matrix) filled with zeros
    my_array = np.zeros((3, 4))
    expected_array = np.array([[0., 0., 0., 0.],
                               [0., 0., 0., 0.],
                               [0., 0., 0., 0.]])

    assert np.array_equal(my_array, expected_array)


def test_ones():
    # Create a NumPy array filled with ones
    my_array = np.ones(5)
    expected_array = np.array([1, 1, 1, 1, 1])
    assert np.array_equal(my_array, expected_array)


def test_linspace():
    # Create a NumPy array with 6 evenly spaced numbers from 0 to 1
    my_array = np.linspace(0, 1, 3)
    expected_array = np.array([0., 0.5, 1.])
    assert np.array_equal(my_array, expected_array)

    # Create a NumPy array with 11 evenly spaced numbers from -5 to 5
    my_array = np.linspace(-5, 5, 11)
    expected_array = np.array(
        [-5., -4., -3., -2., -1., 0., 1., 2., 3., 4., 5.])
    assert np.array_equal(my_array, expected_array)
