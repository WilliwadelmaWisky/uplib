from src.uplib import minmax, standard, origin_error
from numpy import array
from math import isclose


def test_minmax() -> None:
    """
    A couple of tests for minmax-method
    :return: None
    """
    assert isclose(minmax(lambda x, y: x + y, array([1, 2]), array([0.2, 0.5])), 0.7, abs_tol=0.01)
    assert isclose(minmax(lambda x, y: x - y, array([1, 2]), array([0.2, 0.5])), 0.7, abs_tol=0.01)
    assert isclose(minmax(lambda x, y, z, w: x + y + z + w, array([1, 2, 3, 4]), array([0.2, 0.5, 0.3, 0.1])), 1.1, abs_tol=0.01)
    assert isclose(minmax(lambda x, y: x**2 * y**2, array([1, 2]), array([0.2, 0.3])), 3.617, abs_tol=0.01)


def test_standard() -> None:
    """
    A couple of tests for standard-method
    :return: None
    """
    assert isclose(standard(lambda x, y: x + y, array([1, 2]), array([0.2, 0.5])), 0.5385, abs_tol=0.01)
    assert isclose(standard(lambda x, y: x**2 + 2 * y, array([1, 2]), array([0.2, 0.5])), 1.0770, abs_tol=0.01)
    assert isclose(standard(lambda x, y: 3 / 2 * x**4 + 2 / 5 * y**3, array([1, 2]), array([0.2, 0.5])), 2.6832, abs_tol=0.01)
    assert isclose(standard(lambda x, y: x**2 * y, array([1, 2]), array([0.2, 0.5])), 0.9433, abs_tol=0.01)
    assert isclose(standard(lambda x, y: x ** 2 * y**2, array([1, 2]), array([0.2, 0.3])), 2, abs_tol=0.01)


def test_origin_error() -> None:
    """
    A couple of tests for origin_error
    :return: None
    """
    assert isclose(origin_error(lambda x, a, b: a * x + b, array([1, 2, 3]), array([1, 1.5, 2])), 0.5, abs_tol=0.01)
    assert isclose(origin_error(lambda x, a, b: a * x ** 2 + b, array([1, 2, 3]), array([2, 5, 10])), 1.0, abs_tol=0.01)
    assert isclose(origin_error(lambda x, b: 2 * x + b, array([1, 2, 3]), array([3, 5, 7])), 1.0, abs_tol=0.01)
