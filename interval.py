import numpy as np
import matplotlib.pyplot as plt


class Interval():
    """
    A class representing a closed interval of real numbers.
    This class can undergo arithmetic operations with other intervals,
    and of real numbers, where a real number n is represented as [n, n].
    """
    def __init__(self, *args):
        """
        Initializes an interval
        Given one numeric parameter
        """
        left = args[0]
        if len(args) > 1:
            right = args[1]
        else:
            right = args[0]
        if not is_number(left) or not is_number(right):
            raise ValueError("arguments must be numbers")
        if left <= right:
            self.left = left
            self.right = right
        else:
            self.right = left
            self.left = right

    def __add__(self, other):
        """
        Adds this interval to another interval
        """
        other = as_interval(other)
        return Interval(self.left + other.left, self.right + other.right)

    def __radd__(self, other):
        """
        The reverse order of the add method
        Addition of intervals is commutative
        """
        return self + other

    def __sub__(self, other):
        """
        Subtracts another interval from this interval
        """
        other = as_interval(other)
        return Interval(self.left - other.right, self.right - other.left)
    
    def __rsub__(self, other):
        """
        Subtracts this interval from another interval
        """
        return as_interval(other) - self

    def __mul__(self, other):
        """
        Multiplies this interval with another interval
        """
        other = as_interval(other)
        combinations = [self.left * other.left, self.left * other.right, self.right * other.left, self.right * other.right]
        return Interval(min(combinations), max(combinations))

    def __rmul__(self, other):
        """
        Multiplies another interval with this interval
        Multiplication commutes
        """
        return self * other

    def __div__(self, other):
        """
        Divides this interval by another interval
        """
        other = as_interval(other)
        combinations = [self.left / other.left, self.left / other.right, self.right / other.left, self.right / other.right]
        return Interval(min(combinations), max(combinations))

    def __pow__(self, power):
        """
        Takes this interval to an integer power
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
    Returns x, inputted as either a number or an interval, as an interval.
    If x is an interval the function returns just x. 
    """
    if isinstance(x, Interval):
        return x
    return Interval(x)

def p(i):
    """
    The interval polynomial defined in the problem description.
    Returns an interval resulting from the interval parameter.
    """
    return 3 * i**3 - 2 * i**2 - 5 * i - 1

def is_number(x):
    """
    Given a data value, returns True if it is of type float or int, False otherwise.
    """
    return isinstance(x, int) or isinstance(x, float)


def main():
    """
    Main function;
    For testing and demonstrative purposes.
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

    plt.xlabel("x")
    plt.ylabel("p(I)")

    plt.title("$p(I) = 3I^3 - 2I^2 - 5I - 1$, I = Interval(x, x + 0.5)")

    plt.plot(x, y_lower)
    plt.plot(x, y_upper)
    plt.savefig("interval.png")
    

if __name__ == "__main__":
    main()
    