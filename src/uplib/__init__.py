from typing import Callable
from scipy.optimize import curve_fit
from numpy import zeros, abs, max, where, ndarray
from math import floor, sqrt
from .util import partial_df


def minmax(func: Callable[[ndarray], float], point: ndarray | int | float, err: ndarray | int | float,
           full_output: bool = False):
    """
    Calculates an uncertainty using a min-max method, calculation is expensive because it uses bruteforce approach
    :param func: Function to apply min-max method
    :param point: All the variables required in a function arguments
    :param err: All the errors to variables, has to be of same size as value_data array
        (so even if a variable has an uncertainty of 0 it needs to be added to the array)
    :param full_output: Used to return extra information when set to TRUE
    :return: Calculated error. If full_output is set to TRUE returns a tuple of values.
        The first value is the calculated error, sthe second value is an array of (numbers) value
        configurations (0 = default, 1 = min, 2 = max). Index of the array indicates position of the argument
        (ex. f(x, y) -> [0, 1], meaning x=default, y=min)
    """
    val_count = len(point)
    config_count = 3 ** len(point)
    val_configs = zeros((config_count, val_count))
    fvalues = zeros(config_count)

    for i in range(0, config_count):
        values = zeros(val_count)
        for j in range(0, val_count):
            val_configs[i, j] = floor(i / 3 ** j) % 3
            match int(val_configs[i, j]):
                case 0:
                    values[j] = point[j]
                case 1:
                    values[j] = point[j] - err[j]
                case 2:
                    values[j] = point[j] + err[j]

        fvalues[i] = func(*values)

    refrence_fvalue = func(*point)
    ferrors = abs(fvalues - refrence_fvalue)
    max_error = max(ferrors)

    if not full_output:
        return max_error

    max_error_index = where(ferrors == max_error)[0][0]
    max_error_config = val_configs[max_error_index]
    return err, max_error_config


def standard(func: Callable[[ndarray], float], point: ndarray | int | float, point_err: ndarray | int | float) -> float:
    """
    Calculate the uncertainty with a standard uncertainty propagation method
    :param func: Function
    :param point: Values of function parameters (list or tuple).
    :param point_err: Errors of values (list or tuple).
        If a value has 0 uncertainty, it must still be included in the list
    :return: Calculated error
    """
    error = 0.0
    for i in range(0, len(point)):
        error += (partial_df(func, point, i) * point_err[i]) ** 2

    return sqrt(error)


def origin_error(func: Callable, xdata: ndarray, ydata: ndarray) -> float:
    """
    Calculate the the value of the function at the origin
    :param func: Function to test
    :param xdata: Data of the function input values
    :param ydata: Data of the function output values
    :return: Value of the function at the origin
    """
    popt, _ = curve_fit(func, xdata, ydata)
    return func(0, *popt)
