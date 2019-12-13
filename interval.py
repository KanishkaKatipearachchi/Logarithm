"""
Things remaining to be done:
--Documentation
--Abstraction of numbers as intervals
----One can construct an interval with one argument, making an "empty" interval; 
----We can also add a constructor that creates an interval from an interval
--Parameter error raising in operators to ensure no unintended behavior
--Other TODO throughout the code
"""
import numpy as np
import matplotlib.pyplot as plt


class Interval():
    """
    A class representing a closed interval of real numbers
    """
    def __init__(self, *args):
        """
        TODO: add proper assertions/exception throws 
        such that the arguments can only be floats or an Inverval
        """
        left = args[0]
        if len(args) > 1:
            right = args[1]
        else:
            right = args[0]
        try:
            left = float(left)
            right = float(right)
        except:
            raise ValueError("arguments must be castable to type float")
        if left <= right:
            self.left = left
            self.right = right
        else:
            self.right = left
            self.left = right

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.left + other.left, self.right + other.right)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = as_interval(other)
        return Interval(self.left - other.left, self.right - other.right)
    
    def __rsub__(self, other):
        return as_interval(other) - self

    def __mul__(self, other):
        other = as_interval(other)
        """
        TODO: try to clean this up? Make it more compressed?
        Is it true that for all real numbers that the product of the rights is greater than any other of the products?
        """
        return Interval(min([self.left * other.left, self.left * other.right, self.right * other.left, self.right * other.right]),
                max([self.left * other.left, self.left * other.right, self.right * other.left, self.right * other.right]))

    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        other = as_interval(other)
        """
        TODO: same as mul; 
        Also, better way to handle div by zero errors?
        """
        return Interval(min([self.left / other.left, self.left / other.right, self.right / other.left, self.right / other.right]),
                max([self.left / other.left, self.left / other.right, self.right / other.left, self.right / other.right]))

    def __pow__(self, power):
        """
        TODO: The definition is a bit odd;
        It looks as though it can only be defined for integer powers
        """
        if type(power) != int:
            raise ValueError("power must be an integer")
        if power % 2 == 0:
            if self.left >= 0:
                return Interval(self.left**power, self.right**power)
            elif self.right < 0:
                return Interval(self.right**power, self.left**power)
            else:
                return Interval(0, max([self.right**power, self.left**power]))
        return Interval(self.left**power, self.right**power)

    def __contains__(self, item):
        return item >= self.left and item <= self.right

    def __str__(self):
        return "[%s, %s]" % (self.left, self.right)

def as_interval(x):
    """
    Returns x, inputted as either a number or an interval, as an interval
    If x is an interval the function returns x
    """
    if isinstance(x, Interval):
        return x
    return Interval(float(x))

def p(i):
    """
    The interval polynomial defined in the problem description
    """
    return 3 * i**3 - 2 * i**2 - 5 * i - 1


def main():
    """
    Main function;
    For testing purposes only
    """
    i1 = Interval(1, 4)
    print(i1)
    i2 = Interval(-2, -1)
    print(i2)
    print(i1 + i2)
    print(i1 - i2)
    print(i1 * i2)
    print(i1 / i2)
    print(Interval(2, 3) + 1)
    print(1 + Interval(2, 3))
    print(Interval(2, 3) - 1)
    print(1 - Interval(2, 3))
    print(Interval(2, 3) * 1)
    print(1 * Interval(2, 3))
    x = Interval(-2, 2)
    print(x**2)
    print(x**3)

    x = np.linspace(0.0, 1, 1000)

    y_intervals = [p(Interval(x[i], x[i] + 0.5)) for i in range(len(x))]
    y_lower = [i.left for i in y_intervals]
    y_upper = [i.right for i in y_intervals]

    plt.plot(x, y_lower)
    plt.plot(x, y_upper)
    plt.savefig("interval.png")
    

if __name__ == "__main__":
    main()
    