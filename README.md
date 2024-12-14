# Uncertainty Propagation Library (uplib)
![Version](https://img.shields.io/badge/python-3.0+-blue.svg?style=flat)
![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat)

<p align="justify">
    A python library for calculating uncertainties. The library features a couple of methods to speed up the uncertainty analysis during and after measurements. All of the methods assume the variables to be independent, no correlation is considered. Testing is done via the *pytest* framework.
</p>

- Built for personal-use, so the codebase is not the cleanest!
- There is no PyPI package available!

## Getting Started
### Dependencies
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=flat&logo=scipy&logoColor=%white)

### Installation
Install the dependencies to your project.

```
pip install numpy scipy
```

Clone the repository.

```
git clone https://github.com/WilliwadelmaWisky/uplib.git
```

Copy `lib.py` file to your project.

## Features
> ![NOTE]
> The import statements used in the examples may vary depending on where the files are located!

### Standard
Uses the standard uncertainty propagation method and is very useful for calculating a realistic error value at a certain point. A good way of calculating an uncertainty of a variable. An example of calculating an uncertainty of a function $f(x, y) = x^2 \cdot y^2$ at $x = (1.0 \pm 0.2)$ and $y = (2.0 \pm 0.3)$ using the standard uncertainty propagation method.

```python
from uplib import standard
from numpy import array

# Define the function f
f = lambda x, y: x ** 2 * y ** 2

# Define the points
point = array([1.0, 2.0])

# Define the errors of points
point_err = array([0.2, 0.3])

# Use the standard uncertainty propagation method
err = standard(f, point, point_err) 

# err = 2.0
```

### Minmax
Uses the minmax uncertainty propagation method. It is very handy for quickly determining maximum value the error can be. Not ideal for calculating realistic uncertainties, use standard instead for that. An example of calculating an uncertainty of a function $f(x, y) = x^2 \cdot y^2$ at $x = (1.0 \pm 0.2)$ and $y = (2.0 \pm 0.3)$ using a minmax uncertainty propagation method.

```python
from uplib import minmax
from numpy import array

# Define the function f
f = lambda x, y: x ** 2 * y ** 2

# Define the points
point = array([1.0, 2.0])

# Define the errors of points
point_err = array([0.2, 0.3])

# Use the minmax uncertainty propagation method
err = minmax(f, point, point_err)

# err = 3.617
```

### Origin Error
Uses graphical methods to calculate the error at the origin $(x = 0)$. It is very useful for quickly testing if a systematic error occurs in the measuring equipment. An example of calculating an uncertainty of the origin. A theoretical function of the measurement is $f(x) = 2x$. The data of the measurements are in the following table.

|   x   |   y   |
|:-----:|:-----:|
|  1.0  |  3.0  |
|  2.0  |  5.0  |
|  3.0  |  7.0  |

```python
from uplib import origin_error
from numpy import array

# Define a linear function to be fitted
f = lambda x, b: 2 * x + b

# Define the x and y coordinates of points
xdata = array([1.0, 2.0, 3.0])
ydata = array([3.0, 5.0, 7.0])

# Use origin_error to calculate the systematic error, in other words the value of b
err = origin_error(f, xdata, ydata)

# err = 1.0
# By looking at the function, we can see that at x = 0, y should also be 0.
# Thus we have found a systematic error in the measurement equipment.
```
