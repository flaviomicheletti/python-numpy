import numpy as np


def test_math_operations1():
    # Create two NumPy arrays
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    # Perform mathematical operations on the arrays
    c = a + b  # element-wise addition
    d = a * b  # element-wise multiplication
    e = a / b  # element-wise division

    # Check that the results are correct
    assert np.all(c == np.array([5, 7, 9]))
    assert np.all(d == np.array([4, 10, 18]))

    """ We use the `allclose()` function to check that the elements of the `e`
    array are close to the expected values within a certain tolerance. 
    This ensures that the test passes even if there is some small numerical 
    error in the calculation."""
    assert np.allclose(e, np.array([0.25, 0.4, 0.5]), rtol=1e-05, atol=1e-08)


def test_math_operations2():
    """The `np.all()` function is a NumPy function that returns `True` if all
    elements in an array evaluate to `True`, and `False` otherwise. It takes a
    single argument, which is the array to be checked."""

    # Example 1: Check if all elements are nonzero
    a = np.array([1, 2, 3])
    b = np.array([1, 0, 4])
    assert np.all(a) == True
    assert np.all(b) == False

    # Example 2: Check if all elements are even
    c = np.array([2, 4, 6])
    d = np.array([2, 4, 5])
    assert np.all(c % 2 == 0) == True
    assert np.all(d % 2 == 0) == False

    # Example 3: Check if all elements in a 2D array are greater than a threshold
    e = np.array([[1, 2, 3], [4, 5, 6]])
    f = np.array([[7, 8, 9], [6, 5, 4]])
    assert np.all(e > 2) == False
    assert np.all(f > 2) == True


def test_matrix_multiplication():
    """We then perform matrix multiplication on the arrays using the `np.dot()`
    function, which results in a new array `c`.

    Matrix multiplication is an important operation in linear algebra and is
    used in a variety of applications, such as solving systems of linear
    equations and in machine learning algorithms like neural networks.

    The `np.dot()` function is a versatile function in NumPy that can perform
    matrix multiplication, as well as dot product, inner product, and other
    types of matrix operations."""

    # Create two NumPy arrays
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    # Perform matrix multiplication on the arrays
    c = np.dot(a, b)

    # Check that the result is correct
    expected_result = np.array([[19, 22], [43, 50]])
    assert np.all(c == expected_result)


def test_mean_and_std():
    """We then use the `np.mean()` function to calculate the mean of the array,
    and the `np.std()` function to calculate the standard deviation of the
    array"""

    # Create a NumPy array
    a = np.array([1, 2, 3, 4, 5])

    # Calculate the mean and standard deviation of the array
    mean_a = np.mean(a)
    std_a = np.std(a)

    # Check that the results are correct
    assert np.isclose(mean_a, 3.0, rtol=1e-05, atol=1e-08)
    assert np.isclose(std_a, 1.4142135623730951, rtol=1e-05, atol=1e-08)


def test_isclose():
    # Example 1: Check if two arrays are element-wise equal within a tolerance
    a = np.array([1, 2, 3])
    b = np.array([1.1, 2.2, 3.3])
    c = np.array([1.01, 2.02, 3.03])
    assert np.all(np.isclose(a, b, rtol=0.1, atol=0.1) == np.array([True, True, True]))
    assert np.all(np.isclose(a, c) == np.array([False, False, False]))

    # Example 2: Check if a scalar is within a certain range of another scalar
    x = 1.23
    y = 1.25
    assert np.isclose(x, y, rtol=0.1, atol=0.02) == True
    assert np.isclose(x, y) == False

    # Example 3: Check if two arrays are element-wise equal with default tolerance
    d = np.array([1.00001, 2.00002, 3.00003])
    e = np.array([1.000011, 2.000023, 3.000035])
    assert np.all(np.isclose(d, e) == np.array([True, True, True]))

