# Uncertainty Propagation Library (uplib)
A python library for calculating uncertainties.
The library features a couple of methods to speed up the uncertainty analysis during measurements.
All of the methods assume the variables to be independent.
Testing is done via the *pytest* framework.

- Built for personal-use, so the codebase is not the cleanest!
- There is no PyPI package available!

Version 1.0

## Installation
- Make sure to have the depencies installed, **Numpy and Scipy!**
- Download the `.zip` -file (of the desired version) from releases
- Unzip the file and paste the contents to your project

## Features
**The import statements used in the examples may vary depending on where the files are located!**

### Standard
Uses the standard uncertainty propagation method and is very useful for calculating a realistic error value at a certain point.

**Assignment:**
Calculate an uncertainty of a function `f(x, y) = x^2 * y^2` at `x = (1.0 ± 0.2)` and `y = (2.0 ± 0.3)` using a standard uncertainty propagation method.

**Answer:**
```python
from src.uplib import standard
from numpy import array

f = lambda x, y: x ** 2 * y ** 2
point = array([1.0, 2.0])
point_err = array([0.2, 0.3])

err = standard(f, point, point_err) 

# err = 2.0
```

### Minmax
Uses the minmax uncertainty propagation method. It is very handy for determining maximum value the error can be.

**Assignment:** 
Calculate an uncertainty of a function `f(x, y) = x^2 * y^2` at `x = (1.0 ± 0.2)` and `y = (2.0 ± 0.3)` using a minmax uncertainty propagation method.

**Answer:**
```python
from src.uplib import minmax
from numpy import array

f = lambda x, y: x ** 2 * y ** 2
point = array([1.0, 2.0])
point_err = array([0.2, 0.3])

err = minmax(f, point, point_err)

# err = 3.617
```

### Origin Error
Uses graphical methods to calculate the error at the origin. It is very useful for quickly testing if systematic error occurs in the measuring equipment.

**Assignemt:** 
Calculate an uncertainty of the origin of a function `f(x) = 2x`. 
The data of the measurements are in the following table.

|   x   |   y   |
|:-----:|:-----:|
|  1.0  |  3.0  |
|  2.0  |  5.0  |
|  3.0  |  7.0  |

**Answer:**
```python
from src.uplib import origin_error
from numpy import array

f = lambda x, b: 2 * x + b
xdata = array([1.0, 2.0, 3.0])
ydata = array([3.0, 5.0, 7.0])

err = origin_error(f, xdata, ydata)

# err = 1.0
# By looking at the function, we can see that at x = 0, y should also be 0.
# Thus we have found a systematic error in the measurement equipment.
```
