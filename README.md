# Uncertainty Propagation Library (uplib)
A python library for calculating uncertainties. The library features a couple of methods to speed up the uncertainty analysis during and after measurements. All of the methods assume the variables to be independent, no correlation is considered. Testing is done via the *pytest* framework.

- Built for personal-use, so the codebase is not the cleanest!
- There is no PyPI package available!

Version 1.0.0

## Getting Started
- Make sure to have the depencies installed, **Numpy and Scipy!**.
- Download the `.zip` from releases or optionally copy paste the contents of `lib.py` to your project.

## Features
**The import statements used in the examples may vary depending on where the files are located!**

### Standard
Uses the standard uncertainty propagation method and is very useful for calculating a realistic error value at a certain point. A good way of calculating an uncertainty of a variable.

**Assignment:**
Calculate an uncertainty of a function $f(x, y) = x^2 \cdot y^2$ at $x = (1.0 \pm 0.2)$ and $y = (2.0 \pm 0.3)$ using a standard uncertainty propagation method.

**Answer:**
```python
from uplib import standard
from numpy import array

f = lambda x, y: x ** 2 * y ** 2
point = array([1.0, 2.0])
point_err = array([0.2, 0.3])

err = standard(f, point, point_err) 

# err = 2.0
```

### Minmax
Uses the minmax uncertainty propagation method. It is very handy for quickly determining maximum value the error can be. Not ideal for calculating realistic uncertainties, use standard instead for that.

**Assignment:** 
Calculate an uncertainty of a function $f(x, y) = x^2 \cdot y^2$ at $x = (1.0 \pm 0.2)$ and $y = (2.0 \pm 0.3)$ using a minmax uncertainty propagation method.

**Answer:**
```python
from uplib import minmax
from numpy import array

f = lambda x, y: x ** 2 * y ** 2
point = array([1.0, 2.0])
point_err = array([0.2, 0.3])

err = minmax(f, point, point_err)

# err = 3.617
```

### Origin Error
Uses graphical methods to calculate the error at the origin $(x = 0)$. It is very useful for quickly testing if a systematic error occurs in the measuring equipment.

**Assignemt:** 
Calculate an uncertainty of the origin of a function $f(x) = 2x$. 
The data of the measurements are in the following table.

|   x   |   y   |
|:-----:|:-----:|
|  1.0  |  3.0  |
|  2.0  |  5.0  |
|  3.0  |  7.0  |

**Answer:**
```python
from uplib import origin_error
from numpy import array

f = lambda x, b: 2 * x + b
xdata = array([1.0, 2.0, 3.0])
ydata = array([3.0, 5.0, 7.0])

err = origin_error(f, xdata, ydata)

# err = 1.0
# By looking at the function, we can see that at x = 0, y should also be 0.
# Thus we have found a systematic error in the measurement equipment.
```
